<!--signupView.vue-->
<template>
    <div class="sign-in-container">
      <div class="sign-in-box">
        <img src="@/assets/spotify.jpeg" alt="Spotify Logo" class="spotify-logo">
        <h1>Log in to Tunify with Spotify</h1>
        <p>To continue, log in to Spotify. Tunify does not save your account or personal information.</p>
        <button @click="authButton" class="sign-in-button">
          Sign in with Spotify
        </button>
      </div>
    </div>
    <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
</template>
  
<script lang="js">
import apiClient from '@/api.js';
  export default {
    data() {
      return {
        authUrl: null,
        errorMessage: null
      }
    },
    mounted() {
      const tokenValid = localStorage.getItem('authCode')
      if (tokenValid !== null) {
        this.$router.replace('/trending')
      } else {
        this.getAuthURL()
      }
    },
    methods: {
      async getAuthURL() {
        try {
          let response = await apiClient.login();
          if (response.status === 200) {
            this.authUrl = response.data.url;
          }
        } catch (error) {
          console.error("Erreur lors de la récupération de l'URL d'authentification:", error);
          this.errorMessage = "Une erreur s'est produite lors de la connexion. Veuillez réessayer.";
        }
      },
      authButton() {
        if (this.authUrl) {
          window.location.href = this.authUrl;
        } else {
          console.error("URL d'authentification non disponible");
        }
      }
    }
  }
</script>

  
  <style scoped>
    .sign-in-container {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
  
    .sign-in-box {
        background: white;
        padding: 40px 60px;
        border-radius: 8px;
        text-align: center;
        width: 400px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    }
  
    .spotify-logo {
      width: 100px;
      margin-bottom: 20px;
    }
  
    h1 {
      margin-bottom: 20px;
      font-size: 24px;
    }
  
    .sign-in-button {
      background-color: #1DB954;
      color: white;
      padding: 10px 20px;
      border-radius: 25px;
      border: none;
      font-size: 16px;
      font-weight: bold;
      cursor: pointer;
      transition: all 0.3s ease;
    }
  
    .sign-in-button:hover {
      background-color: #189C43; 
    }
  </style>

