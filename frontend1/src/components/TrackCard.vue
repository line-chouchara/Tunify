<!-- TrackCard.vue -->
<template>
    <div class="track-card">
      <img :src="track.album_image" alt="Album Image" class="album-image">
      <div class="track-details">
        <h3 class="track-title">{{ track.title }}</h3>
        <p class="track-artist">{{ track.artist }}</p>
        <a :href="track.spotify_link" target="_blank" rel="noopener">Écouter sur Spotify</a>
      </div>
    </div>
  </template>

<script>
export default {
  props: {
    track: {
      type: Object,
      required: true
    }
  }
}
</script>


<style scoped>
.tracks-container {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  padding: 20px;
  justify-content: center; 
}

.track-card {
  width: 200px;
  border: none;
  border-radius: 8px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  opacity: 0;  /* Initial state: hidden */
  transform: translateY(30px);  /* Initial state: slightly moved down */
  animation: fadeInUp 0.5s forwards 0.2s;  /* Animation to control appearance */
}

.track-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1);
}

.album-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.track-details {
  padding: 15px;
  background: #fafafa;
}

.track-title {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 8px;
}

.track-artist {
  font-size: 15px;
  color: #777;
  margin-bottom: 12px;
}

.track-details a {
  display: inline-block;
  padding: 8px 12px;
  border-radius: 20px;
  background: #1DB954;  /* Spotify green */
  color: white;
  text-decoration: none;
  transition: background 0.3s ease;
}

.track-details a:hover {
  background: #1ED760;  /* Slightly lighter shade for hover */
}
.spotify-link {
  font-size: 14px;
  color: #1DB954; /* Spotify Green */
  text-decoration: none;
  transition: color 0.2s ease;
}

.spotify-link:hover {
  text-decoration: underline;
  color: #1ED760; /* Lighter Spotify Green */
}

@keyframes fadeInUp {
  to {
    opacity: 1;
    transform: translateY(0);
    }
}

</style>