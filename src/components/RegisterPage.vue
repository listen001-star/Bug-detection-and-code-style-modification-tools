<template>
  <div>
    <h2>Register</h2>
    <form @submit.prevent="handleRegister">
      <div>
        <label>Username:</label>
        <input type="text" v-model="username" required />
      </div>
      <div>
        <label>Email:</label>
        <input type="email" v-model="email" required />
      </div>
      <div>
        <label>Password:</label>
        <input type="password" v-model="password" required />
      </div>
      <button type="submit">Register</button>
    </form>
    <button @click="$emit('switch', 'login')">Go to Login</button>
  </div>
</template>

<script>
export default {
  name: 'RegisterPage', // 使用多词名称
  data() {
    return {
      username: '',
      email: '',
      password: ''
    }
  },
  methods: {
    handleRegister() {
      alert(`Registering with ${this.username}`);
    }
  }
}
</script>

<style scoped>
/* 样式保持不变 */
.form-container { max-width: 400px; margin: auto; }
.form-group { margin-bottom: 1em; }
button { width: 100%; }
</style>
