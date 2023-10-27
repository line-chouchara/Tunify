from fastapi import FastAPI, Request, Depends,  HTTPException
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware


app = FastAPI()

# Ajout du middleware de session
app.add_middleware(SessionMiddleware, secret_key="GxcXkpH_thLGZts3Ix1CTtDnh8J7CP90Bka4JvDtb1c") 

# Configuration CORS
origins = [
    "http://localhost:8080",   # url frontend
    "http://192.168.0.12:8080/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Configuration OAuth2 pour Spotipy
sp_oauth = SpotifyOAuth(client_id="405af389753141afa2930afb121143a8",
                        client_secret="1cbcbee8777946c3b30d770a203f487d",
                        redirect_uri="http://localhost:8000/callback",
                        scope="user-library-read user-read-recently-played")


@app.get("/")
def read_root():
    return {"Hello": "World"}

# Route d'authentification pour rediriger vers la page de connexion Spotify
@app.get("/login")
def login(request: Request):
    auth_url = sp_oauth.get_authorize_url()
    return {"url": auth_url}

# Route de déconnexion pour supprimer le token de la session
@app.get("/logout")
def logout(request: Request):
    request.session.pop('token_info', None)
    return {"message": "Déconnexion réussie!"}

@app.get("/trending")
def trending():
    return {"message": "Page Trending"}


# Route de rappel pour récupérer le token après connexion réussie
@app.get("/callback")
def callback(request: Request, code: str = None):
    print(f"Code received: {code}")  # Debug
    token_info = sp_oauth.get_access_token(code)
    print("Storing token in session", token_info)  # Debug
    request.session['token_info'] = token_info
    
    # Redirigez vers la page "trending" de votre application Vue.js
    access_token = token_info["access_token"]
    return RedirectResponse(url=f"http://localhost:8080/callback#access_token={access_token}")


# Fonction pour récupérer le token actuel
def get_current_token(request: Request):
    token_info = request.session.get('token_info', {})
    access_token = token_info.get('access_token')
    refresh_token = token_info.get('refresh_token')
    
    print(f"Current token: {access_token}")

    if "expires_at" in token_info and sp_oauth.is_token_expired(token_info):
        print("Token has expired. Refreshing...")
        new_token_info = sp_oauth.refresh_access_token(refresh_token)
        print(f"New token: {new_token_info['access_token']}")
        request.session['token_info'] = new_token_info
        access_token = new_token_info['access_token']

    if not access_token:
        # Redirigez vers la page de connexion si le token est None
        raise HTTPException(status_code=401, detail="Authentication token is missing. Please log in again.")

    return access_token

# Une dépendance pour récupérer le client spotipy authentifié
def get_spotify_client(token: str = Depends(get_current_token)):
    if not token:
        raise HTTPException(status_code=401, detail="Authentication token is missing. Please log in again.")
        
    print(f"Using token for spotipy client: {token}")
    return spotipy.Spotify(auth=token)



# Route pour récupérer les morceaux sauvegardés de l'utilisateur
@app.get("/tracks")
def get_tracks(sp: spotipy.Spotify = Depends(get_spotify_client)):
    results = sp.current_user_saved_tracks()
    return results


#fonction pour récupérer les morceaux récemment écoutés par l'utilisateur et filtrert les données pertinents,
def transform_tracks(spotify_data):
    transformed_tracks = []

    for item in spotify_data["items"]:
        track = item["track"]
        transformed_track = {
            "title": track["name"],
            "artist": track["artists"][0]["name"],  
            "album_image": track["album"]["images"][0]["url"],  
            "spotify_link": track["external_urls"]["spotify"]
        }
        transformed_tracks.append(transformed_track)

    return transformed_tracks

# Route pour récupérer les morceaux récemment écoutés par l'utilisateur, 
@app.get("/recent-tracks")
def get_recent_tracks(request: Request, sp: spotipy.Spotify = Depends(get_spotify_client)):
    token = get_current_token(request)
    print(f"Using token: {token}")
    raw_data = sp.current_user_recently_played()
    return transform_tracks(raw_data)


# Define a new endpoint for song recommendations
@app.get("/artist-recommendations")
def get_artist_recommendations(sp: spotipy.Spotify = Depends(get_spotify_client)):
    # Make a request to get song recommendations
    recommendations = sp.recommendations()
    # Process and return the recommendations (you can modify this part as needed)
    transformed_recommendations = transform_tracks(recommendations)
    return transformed_recommendations
