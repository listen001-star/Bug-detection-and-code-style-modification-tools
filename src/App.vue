<template>
  <div id="app">
    <component 
      :is="currentPage" 
      @switch="switchPage" 
      @authenticated="currentPage = $event" 
    />
  </div>
</template>

<script>
import LoginPage from './components/LoginPage.vue'
import RegisterPage from './components/RegisterPage.vue'
import MainPage from './components/MainPage.vue'

export default {
  name: 'App',
  data() {
    return {
      currentPage: 'LoginPage'
    }
  },
  components: {
    LoginPage,
    RegisterPage,
    MainPage
  },
  methods: {
    switchPage(page) {
      this.currentPage = page === 'login' ? 'LoginPage' : 'RegisterPage';
    }
  }
}
</script>

<style>
body {
  font-family: Arial, sans-serif;
}
</style>
