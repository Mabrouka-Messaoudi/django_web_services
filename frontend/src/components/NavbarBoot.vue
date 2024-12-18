<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <!-- Web Name -->
      <a class="navbar-brand" href="/">Safrati</a>

      <!-- Mobile Navbar Toggle Button -->
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <!-- Navbar Links -->
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
        <li class="nav-item">
            <router-link to="/" class="nav-link">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/aboutus" class="nav-link">About Us</router-link>
          </li>
        <li class="nav-item">
            <router-link to="/trips" class="nav-link">Trips</router-link>
          </li>
          <li class="nav-item" v-if="!isAuthenticated">
            <router-link to="/login" class="nav-link"  >Login</router-link>
          </li>
          <li class="nav-item" v-if="!isAuthenticated">
            <router-link to="/register" class="nav-link">Register</router-link>
          </li>
          <!-- Show Logout if user is authenticated -->
          <li class="nav-item" v-if="isAuthenticated">
            <a class="nav-link" href="#" @click="logout">Logout</a>
          </li>
          <!-- Show Admin Panel and Logout if user is authenticated -->
          <li class="nav-item" v-if="isAuthenticated ">
            <router-link to="/admin" class="nav-link">Admin Panel</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  
</template>

<script>
export default {
  name: "NavbarBoot",
  computed: {
    // Check if the user is authenticated
    isAuthenticated() {
      return !!localStorage.getItem("auth_token");
      
    },
  },
  methods: {
    // Logout method to remove token and redirect to home
    logout() {
      localStorage.removeItem("auth_token");
      this.$router.push("/");
      window.location.reload(); // Actualise la page pour refléter les changements
    },
  },
  
  
  
};
</script>


<style scoped>
.navbar-brand {
  font-size: 1.8rem;
  font-weight: bold;
}

.nav-link {
  font-size: 1.1rem;
  margin-left: 15px;
  transition: all 0.3s;
}

.nav-link:hover {
  color: #00bcd4;
}
</style>
