<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="handleLogin">
      <div>
        <label>Email:</label>
        <input type="text" v-model="username" required />
      </div>
      <div>
        <label>Password:</label>
        <input type="password" v-model="password" required />
      </div>
      <button type="submit">Login</button>
    </form>
    <button @click="$emit('switch', 'register')">Go to Register</button>
  </div>
</template>

<script>
export default {
  name: 'LoginPage',
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    handleLogin() {
      if (this.username === 'admin' && this.password === '666') {
        this.$emit('authenticated', 'MainPage')
      } else {
        alert('Invalid credentials. Please try again.')
      }
    }
  }
}
</script>

<style scoped>
.form-container { max-width: 400px; margin: auto; }
.form-group { margin-bottom: 1em; }
button { width: 100%; }
</style>
