<template>
  <div id="app">
    <Nav class="mb-5"/>
    <router-view/>
  </div>
</template>

<script>
import Nav from './components/Navbar'

export default {
  name: 'App',
  components: {
    Nav
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=DotGothic16&display=swap');

#app {
  font-family: 'DotGothic16', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
