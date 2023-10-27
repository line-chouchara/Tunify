<!--HomeView.vue-->
<template>
    <div class="container">
      <!-- Introduction section-->
      <section class="introduction">
        <img src="../assets/logo.png" alt="Tunify Logo">
        <h1><span> WELCOME TO TUNIFY</span></h1>
        <p>Tunify is a platform designed for music lovers. Discover new tracks, create playlists, and connect with artists.</p>
  
      </section>
  
      <!-- Card section -->
      <section class="card-section">
        <div class="card">
          <img src="../assets/asset1.png" alt="Discover Image">
          <div class="card-body">
            <h5 class="card-title">Discover</h5>
            <p class="card-text">Input your favorite songs and get personalized recommendations. Engage with our platform and explore new horizons of music.</p>
            
          </div>
        </div>
  
        <div class="card">
          <img src="../assets/asset2.png" alt="Trending Image">
          <div class="card-body">
            <h5 class="card-title">Latest Trends</h5>
            <p class="card-text">Stay updated with the latest trending songs. Be in the loop and never miss out on the latest hits.</p>
           
          </div>
        </div>
  
        <div class="card">
          <img src="../assets/asset3.png" alt="About Image">
          <div class="card-body">
            <h5 class="card-title">About Tunify</h5>
            <p class="card-text">Learn more about our cutting-edge song recommendation system and our mission to redefine music streaming experiences.</p>
           
          </div>
        </div>
      </section>
  
      <!-- Let's start-->
      <div class="join_us">
        <h2><span>Join the platform now!</span></h2>
        <router-link to="/signup" class="btn_join">Sign Up</router-link>
      </div>
    </div>
  </template>
  
  
  <style scoped>
  .container {
    margin: 20px;
  }
  
  .introduction {
    margin-left: 5%;
    padding: 1em;
  }
  
  .card-section {
    display: flex;
    justify-content: space-between;
    margin-top: 2em;
  }
  
  .card {
    width: 30%;
  }
  
  .card img {
    width: 100%;
    height: auto;
  }
  
  .card-body {
    padding: 1em;
  }
  .card-title {
    font-size: 1.5em;
    font-weight: bold;
  }
  
  
  .btn_join {
    background-color: #FD5E64;
    color: white;
    border: 1px solid #FD5E64; /* Made the border color consistent with the background */
    border-radius: 10px;
    padding: 10px 20px; /* Added some padding for better visual appearance */
    font-size: 16px; /* Increased font size for better readability */
    transition: all 0.3s ease; /* Smooth transition for hover effects */
    cursor: pointer; /* Change the cursor to indicate it's clickable */
    text-decoration: none; /* Remove underline if the button is a link */
    display: inline-block; /* Allows the button to respect padding and other inline styles */
  }
  
  .btn_join:hover {
    transform: translateY(-5px);
    background-color: #f97074;
    border-color: #f97074; /* Made the border color consistent with the background on hover */
    color: white; /* Changed text color on hover for contrast */
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2); /* Added a subtle shadow for depth */
  }
  
  </style>
  