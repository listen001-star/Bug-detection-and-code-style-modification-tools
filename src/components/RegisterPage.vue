<template>
  <div class="container d-flex align-items-center justify-content-center vh-100">
    <div class="col-md-6">
      <div class="card p-5 shadow rounded">
        <h2 class="text-center mb-5">Register</h2>
        <form @submit.prevent="handleRegister">
          <div class="form-group mb-4 d-flex align-items-center">
            <label for="username" class="form-label">Username</label>
            <input type="text" id="username" v-model.trim="username" class="form-control flex-grow-1" required />
          </div>
          <div class="form-group mb-4 d-flex align-items-center">
            <label for="email" class="form-label">Email</label>
            <input type="email" id="email" v-model.trim="email" class="form-control flex-grow-1" required />
          </div>
          <div class="form-group mb-4 d-flex align-items-center">
            <label for="password" class="form-label">Password</label>
            <input type="password" id="password" v-model.trim="password" class="form-control flex-grow-1" required />
          </div>
          <button type="submit" class="btn btn-register btn-block mb-4">Register</button>
        </form>
        <div class="text-center">
          <button class="btn btn-login btn-block" @click="$emit('switch', 'login')">Go to Login</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RegisterPage',
  data() {
    return {
      username: '',
      email: '',
      password: ''
    }
  },
  methods: {
    async handleRegister() {
      if (!this.validateEmail(this.email)) {
        alert('Invalid email format.');
        return;
      }

      try {
        const response = await fetch('http://127.0.0.1:8000/api/register', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            username: this.username,
            email: this.email,
            password: this.password
          })
        });

        const data = await response.json();

        if (response.ok && data.success) {
          alert('Registration successful! Please login.');
          this.$emit('switch', 'login');
        } else {
          alert(data.message || 'Registration failed. Please try again.');
        }
      } catch (error) {
        alert('Registration failed. Please try again later.');
        console.error(error);
      }
    },
    validateEmail(email) {
      const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return re.test(email);
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
  width: 100px;
  margin-right: 1rem;
  font-weight: 500;
  color: #333;
}

.form-control {
  border-radius: 10px;
  border: 1px solid #ddd;
  padding: 0.75rem;
  flex-grow: 1;
}

.btn-block {
  width: 100%;
  padding: 0.75rem;
  font-size: 1.1rem;
  font-weight: 600;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.btn-register {
  background: linear-gradient(to right, #43cea2, #185a9d);
  color: #fff;
  border: none;
}

.btn-register:hover {
  background: linear-gradient(to right, #3aa187, #134a7b);
}

.btn-login {
  background: linear-gradient(to right, #6a11cb, #2575fc);
  color: #fff;
  border: none;
}

.btn-login:hover {
  background: linear-gradient(to right, #5e0eb3, #1f5ccc);
}

.mb-4 {
  margin-bottom: 1.5rem !important;
}
</style>
