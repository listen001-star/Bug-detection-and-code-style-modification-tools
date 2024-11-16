<template>
  <div class="container d-flex align-items-center justify-content-center vh-100">
    <div class="col-md-6">
      <div class="card p-5 shadow rounded">
        <h2 class="text-center mb-5">Login</h2>
        <form @submit.prevent="handleLogin">
          <div class="form-group mb-4 d-flex align-items-center">
            <label for="email" class="form-label">Email</label>
            <input type="text" id="email" v-model.trim="username" class="form-control flex-grow-1" required />
          </div>
          <div class="form-group mb-4 d-flex align-items-center">
            <label for="password" class="form-label">Password</label>
            <input type="password" id="password" v-model.trim="password" class="form-control flex-grow-1" required />
          </div>
          <button type="submit" class="btn btn-login btn-block mb-4">Login</button>
        </form>
        <div class="text-center mb-4">
          <button class="btn btn-register btn-block" @click="$emit('switch', 'register')">Go to Register</button>
        </div>
        <div class="text-center">
          <button class="btn btn-main-page btn-block" @click="goToMainPage">Go to Main Page</button>
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
        const response = await fetch('http://127.0.0.1:8000/api/login', {
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
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

.card {
  border-radius: 15px;
  padding: 2.5rem;
  background: rgba(255, 255, 255, 0.9);
  box-shadow: 0 6px 30px rgba(0, 0, 0, 0.15);
}

h2 {
  color: #333;
  font-size: 1.75rem;
  font-weight: 600;
}

.form-group {
  display: flex;
  align-items: center;
}

.form-label {
  width: 100px; /* 固定标签宽度，确保对齐 */
  margin-right: 1rem; /* 标签与文本框之间的距离 */
  font-weight: 500;
  color: #333;
}

.form-control {
  border-radius: 10px;
  border: 1px solid #ddd;
  padding: 0.75rem;
  flex-grow: 1; /* 让输入框自适应宽度 */
}

.btn-block {
  width: 100%;
  padding: 0.75rem;
  font-size: 1.1rem;
  font-weight: 600;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.btn-login {
  background: linear-gradient(to right, #6a11cb, #2575fc);
  color: #fff;
  border: none;
}

.btn-register {
  background: linear-gradient(to right, #43cea2, #185a9d);
  color: #fff;
  border: none;
}

.btn-main-page {
  background: linear-gradient(to right, #ff7e5f, #feb47b);
  color: #fff;
  border: none;
}

.btn-login:hover {
  background: linear-gradient(to right, #5e0eb3, #1f5ccc);
}

.btn-register:hover {
  background: linear-gradient(to right, #3aa187, #134a7b);
}

.btn-main-page:hover {
  background: linear-gradient(to right, #e76b46, #e29365);
}

.mb-4 {
  margin-bottom: 1.5rem !important;
}
</style>
