<!--trendingView.vue-->
<!-- Trending.vue -->
<template>
    <div class="trending-page">
      <h1 class="trending-title"><span>Trend</span></h1>
      <section class="recent-tracks-section">
        <h2>Recently listened to songs</h2>
      </section>
      <RecentTracks />

    </div>
  </template>
  
  <script>
  import RecentTracks from '@/components/RecentTracks.vue';  
  export default {
    components: {
      RecentTracks
    }
  }
  </script>
  
  <style scoped>
  .trending-page {
    padding: 16px;
  }
  
  .trending-title {
    font-size: 24px;
    margin-bottom: 16px;
  }
  
  .recent-tracks-section {
    margin-top: 32px;
  }
  
  .recent-tracks-section h2 {
    font-size: 20px;
    margin-bottom: 16px;
  }
  </style>
  