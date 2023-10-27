//api.js 
import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000', // URL  backend
  withCredentials: true, 
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json'
  }
});

// Interception des requêtes pour ajouter le token d'authentification
apiClient.interceptors.request.use(config => {
    const tokenData = JSON.parse(localStorage.getItem("authCode"));
    if (tokenData && tokenData.accessToken) {
        config.headers['Authorization'] = `Bearer ${tokenData.accessToken}`;
        console.log("Setting Authorization Header:", config.headers['Authorization']);
    } else {
        console.log("No token found in local storage");
    }
    return config;
}, error => {
    console.error("Error in request interceptor:", error);
    return Promise.reject(error);
});


  

export default {
  login() {
    return apiClient.get('/login');
  },
  logout() {
    return apiClient.get('/logout');
  },
  getTracks() {
    return apiClient.get('/tracks');
  },
  getRecentTracks() {
    return apiClient.get('/recent-tracks');
  },
  getRecommendations() {
    return apiClient.get(`/recommendations`);
}

};
