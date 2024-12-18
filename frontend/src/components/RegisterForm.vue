<template>
  <div class="container my-5">
    <h2 class="text-center mb-4">Create a New Account</h2>
    <div class="row justify-content-center">
      <div class="col-md-6 col-lg-4">
        <div class="card shadow-lg rounded-lg">
          <div class="card-body">
            <form @submit.prevent="register">
              <!-- Username Input -->
              <div class="mb-3">
                <label for="username" class="form-label">Username</label>
                <input type="text" class="form-control" id="username" v-model="username" placeholder="Enter your username" required />
              </div>

              <!-- Email Input -->
              <div class="mb-3">
                <label for="email" class="form-label">Email</label>
                <input type="email" class="form-control" id="email" v-model="email" placeholder="Enter your email" required />
              </div>

              <!-- Nom Input -->
              <div class="mb-3">
                <label for="nom" class="form-label">First Name</label>
                <input type="text" class="form-control" id="nom" v-model="nom" placeholder="Enter your first name" required />
              </div>

              <!-- Prenom Input -->
              <div class="mb-3">
                <label for="prenom" class="form-label">Last Name</label>
                <input type="text" class="form-control" id="prenom" v-model="prenom" placeholder="Enter your last name" required />
              </div>

              <!-- Phone Number Input -->
              <div class="mb-3">
                <label for="num_tel" class="form-label">Phone Number</label>
                <input type="tel" class="form-control" id="num_tel" v-model="num_tel" placeholder="Enter your phone number" required />
              </div>

              <!-- Address Input -->
              <div class="mb-3">
                <label for="adresse" class="form-label">Address</label>
                <textarea class="form-control" id="adresse" v-model="adresse" placeholder="Enter your address" required></textarea>
              </div>

              <!-- Password Input -->
              <div class="mb-3">
                <label for="password" class="form-label">Password</label>
                <input type="password" class="form-control" id="password" v-model="password" placeholder="Enter your password" required />
              </div>

              <!-- Confirm Password Input -->
              <div class="mb-3">
                <label for="confirmPassword" class="form-label">Confirm Password</label>
                <input type="password" class="form-control" id="confirmPassword" v-model="confirmPassword" placeholder="Confirm your password" required />
              </div>

              <!-- Register Button -->
              <div class="d-grid">
                <button type="submit" class="btn btn-success">Register</button>
              </div>
            </form>

            <p class="mt-3 text-center">
              Already have an account? <router-link to="/login">Login here</router-link>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';  // Make sure Axios is imported

export default {
  data() {
    return {
      username: '',
      email: '',
      password: '',
      confirmPassword: '',
      nom: '',
      prenom: '',
      num_tel: '',
      adresse: '',
    };
  },
  methods: {
    async register() {
      if (this.password !== this.confirmPassword) {
        alert("Passwords do not match!");
        return;
      }

      const data = {
        username: this.username,
        email: this.email,
        password: this.password,
        nom: this.nom,
        prenom: this.prenom,
        num_tel: this.num_tel,
        adresse: this.adresse,
      };

      try {
        // Make sure the backend URL matches your API endpoint
        const response = await axios.post("http://127.0.0.1:8000/register/", data);
        localStorage.setItem("auth_token", response.data.token);  // Store the token for authenticated requests
        this.$router.push("/trips");  // Redirect to the trips page after successful registration
      } catch (error) {
        console.error("Registration failed:", error);
        alert("An error occurred during registration. Please try again.");
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