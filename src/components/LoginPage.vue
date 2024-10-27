<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="card p-4 shadow rounded">
          <h2 class="text-center mb-4">Login</h2>
          <form @submit.prevent="handleLogin">
            <div class="form-group">
              <label for="email">Email</label>
              <input type="text" id="email" v-model.trim="username" class="form-control" required />
            </div>
            <div class="form-group">
              <label for="password">Password</label>
              <input type="password" id="password" v-model.trim="password" class="form-control" required />
            </div>
            <button type="submit" class="btn btn-primary btn-block mt-3">Login</button>
          </form>
          <div class="text-center mt-3">
            <button class="btn btn-link" @click="$emit('switch', 'register')">Go to Register</button>
          </div>
          <div class="text-center mt-3">
            <button class="btn btn-outline-secondary" @click="goToMainPage">Go to Main Page</button>
          </div>
        </div>
      </div>
    </div>
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
    async handleLogin() {
      try {
        const response = await fetch('http://your-backend-url/api/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            username: this.username,
            password: this.password
          })
        });

        const data = await response.json();

        if (response.ok && data.success) {
          this.$emit('authenticated', 'MainPage');
        } else {
          alert(data.message || 'Invalid credentials. Please try again.');
        }
      } catch (error) {
        alert('Login failed. Please try again later.');
        console.error(error);
      }
    },
    goToMainPage() {
      this.$emit('authenticated', 'MainPage');
    }
  }
}
</script>

<style scoped>
.container {
  margin-top: 50px;
}

.card {
  border-radius: 15px;
  background: rgba(255, 255, 255, 0.85); /* 白色透明背景 */
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
}

h2 {
  color: #333;
}

.btn-primary {
  background: linear-gradient(to right, #6a11cb, #2575fc);
  border: none;
  transition: all 0.3s ease;
}

.btn-primary:hover {
  background: linear-gradient(to right, #5e0eb3, #1f5ccc);
}

.form-control {
  border-radius: 8px;
  border: 1px solid #ccc;
}
</style>
