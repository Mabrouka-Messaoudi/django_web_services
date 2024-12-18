<template>
  <div class="container my-5">
    <h2 class="text-center mb-4">Client List</h2>
    <div v-if="clients.length > 0" class="list-group">
      <div v-for="client in clients" :key="client.id" class="list-group-item d-flex justify-content-between align-items-center">
        <div>
          <strong>{{ client.username }}</strong><br>
          <span>{{ client.email }}</span><br>
          <span>{{ client.nom }} {{ client.prenom }}</span><br>
          <span>{{ client.num_tel }}</span><br>
          <span>{{ client.adresse }}</span>
        </div>
        <button @click="editClient(client)" class="btn btn-warning btn-sm">Edit</button>
      </div>
    </div>
    <div v-else>
      <p>No clients found.</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      clients: [],
    };
  },
  async created() {
    // Only fetch client list if the user is an admin
    const token = localStorage.getItem('auth_token');
    if (!token) {
      this.$router.push('/login');  // Redirect if not logged in
      return;
    }

    const response = await fetch('http://127.0.0.1:8000/clients/', {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
    });

    if (response.ok) {
      const data = await response.json();
      this.clients = data;
    } else {
      alert('Failed to fetch clients.');
    }
  },
 
    
  
};
</script>

<style scoped>
.list-group-item {
  margin-bottom: 1rem;
}

.btn-warning {
  background-color: #f0ad4e;
}
</style>
