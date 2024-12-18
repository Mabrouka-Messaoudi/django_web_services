<template>
  <div class="container my-5">
    <h2 class="text-center mb-4">Login to Your Account</h2>
    <div class="row justify-content-center">
      <div class="col-md-6 col-lg-4">
        <div class="card shadow-lg rounded-lg">
          <div class="card-body">
            <form @submit.prevent="login">
              <!-- Username Input -->
              <div class="mb-3">
                <label for="username" class="form-label">Username</label>
                <input type="text" class="form-control" id="username" v-model="username" placeholder="Enter your username" required />
              </div>

              <!-- Password Input -->
              <div class="mb-3">
                <label for="password" class="form-label">Password</label>
                <input type="password" class="form-control" id="password" v-model="password" placeholder="Enter your password" required />
              </div>

              <!-- Login Button -->
              <div class="d-grid">
                <button type="submit" class="btn btn-primary" >Login</button>
              </div>
            </form>

            <p class="mt-3 text-center">
              Don't have an account? <router-link to="/register">Register here</router-link>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    async login() {
  try {
    const response = await fetch('http://127.0.0.1:8000/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: this.username,
        password: this.password,
      }),
    });

    if (response.ok) {
      const data = await response.json();
      // Save the auth token to localStorage
      localStorage.setItem('auth_token', data.token);
      // Redirect to the /trips page after successful login
      this.$router.push('/trips');
    } else {
      alert('Invalid credentials');
    }
  } catch (error) {
    console.error("Error logging in:", error);
  }
},
  },
};
</script>

<style scoped>
.card {
  border: none;
  border-radius: 12px;
}

.card-body {
  padding: 2rem;
}

h2 {
  color: #333;
  font-weight: bold;
}

button {
  font-weight: bold;
  transition: all 0.3s;
}

button:hover {
  background-color: #00bcd4;
}
</style>
