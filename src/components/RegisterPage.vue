<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="card p-4 shadow rounded">
          <h2 class="text-center mb-4">Register</h2>
          <form @submit.prevent="handleRegister">
            <div class="form-group">
              <label for="username">Username</label>
              <input type="text" id="username" v-model.trim="username" class="form-control" required />
            </div>
            <div class="form-group">
              <label for="email">Email</label>
              <input type="email" id="email" v-model.trim="email" class="form-control" required />
            </div>
            <div class="form-group">
              <label for="password">Password</label>
              <input type="password" id="password" v-model.trim="password" class="form-control" required />
            </div>
            <button type="submit" class="btn btn-success btn-block mt-3">Register</button>
          </form>
          <div class="text-center mt-3">
            <button class="btn btn-link" @click="$emit('switch', 'login')">Go to Login</button>
          </div>
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
        const response = await fetch('http://your-backend-url/api/register', {
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

.btn-success {
  background: linear-gradient(to right, #43cea2, #185a9d);
  border: none;
  transition: all 0.3s ease;
}

.btn-success:hover {
  background: linear-gradient(to right, #3aa187, #134a7b);
}

.form-control {
  border-radius: 8px;
  border: 1px solid #ccc;
}
</style>
