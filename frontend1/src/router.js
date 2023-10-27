import { createRouter, createWebHistory } from 'vue-router';

import Home from './views/HomeView.vue';
import trending from './views/trendingView.vue';
import callback from './views/callbackView.vue';
import signup from './views/signupView.vue';
import discover from './views/discoverView.vue';
import recenttracks from './components/RecentTracks.vue';


const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/trending',
    name: 'trending',
    component: trending
  },
  {
     path: '/signup',
     name: 'signup',
     component: signup
  },
  {
      path:'/callback',
      name: 'callback',
      component: callback
  },
  {
    path:'/discover',
    name: 'discover',
    component: discover
  },
  {
    path:'/recentracks',
    name: 'recentracks',
    component: recenttracks
  },
    
  
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
