<template>
  <nav id="app">
    <NavBar />
    <router-view></router-view>
    <Footer />
  </nav>
  
</template>

<script>
import NavBar from './components/navbar_comp.vue'  
import Footer from './components/footer_comp.vue'

export default {
  name: 'App',
  components: {
    NavBar,
    Footer,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
