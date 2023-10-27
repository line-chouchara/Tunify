<template>
    <div class="discover-container">
      <div v-if="loading" class="loading">
        Loading...
      </div>
      <div v-if="error" class="error">
        Error fetching data: {{ errorMessage }}
      </div>
  
      <!-- Section for Recommended Tracks -->
      <section v-if="recommendedTracks.length > 0" class="recommendations">
        <h2>Recommended For You</h2>
        <div class="tracks-list">
          <track-card v-for="track in recommendedTracks" :key="track.id" :track="track"></track-card>
        </div>
      </section>
    </div>
</template>
  
<script>
import apiClient from '@/api.js';
import TrackCard from '@/components/TrackCard.vue';  
  
export default {
    components: {
      TrackCard
    },
    data() {
      return {
        recentTracks: [],
        recommendedTracks: [],
        loading: true,
        error: false,
        errorMessage: ''
      }
    },
    computed: {
      // Ensure the data structure for recommended tracks
      formattedRecommendedTracks() {
        return this.recommendedTracks.map(track => {
          return {
            id: track.id || null,
            album_image: track.album_image || '',
            title: track.title || '',
            artist: track.artist || '',
            spotify_link: track.spotify_link || ''
          };
        });
      }
    },
    async mounted() {
      try {
        // Fetch recently played tracks
        const responseRecent = await apiClient.getRecentTracks();
        console.log("Recent Tracks:", responseRecent.data);
        this.recentTracks = responseRecent.data;
  
        // Extract track IDs and fetch recommendations
        const responseRecommendations = await apiClient.getRecommendations();
        console.log("Recommendation Response:", responseRecommendations.data); // Log the raw response
        this.recommendedTracks = [...responseRecommendations.data];  // Spread operator to ensure reactivity

      } catch (error) {
            console.error('Error fetching data:', error);
            this.error = true;
            this.errorMessage = error.message || 'Unknown error.';
            if (error.response) {
                console.error('API response:', error.response.data);
            }
      } finally {
        this.loading = false;
      }
    }
}
</script>

<style>
.loading {
  font-size: 1.5rem;
  text-align: center;
  padding: 2rem 0;
}

.error {
  font-size: 1.2rem;
  text-align: center;
  color: red;
  padding: 2rem 0;
}

  .discover-container {
    padding: 20px;
  }
  
  .recently-played, .recommendations {
    margin-bottom: 30px;
  }
  
  h2 {
    font-size: 24px;
    margin-bottom: 15px;
    color: #333;
  }
  
  .tracks-list {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
  }
  </style>
  