<template>
  <div class="container my-5">
    <h1 class="text-center mb-4">Your Reservations</h1>

    <div v-if="!isAuthenticated" class="alert alert-danger text-center">
      You need to be logged in to view your reservations. Please <a href="/login">Login</a> first.
    </div>

    <div v-else>
      <div v-if="reservations.length === 0" class="alert alert-warning text-center">
        You have no reservations.
      </div>

      <div v-else>
        <div class="row">
          <div v-for="(reservation, index) in reservations" :key="reservation.id" class="col-md-4 mb-4">
            <div class="card shadow-sm">
              <img :src="getTripImage(index)" class="card-img-top" alt="Trip image" />
              <div class="card-body">
                <h5 class="card-title">{{ reservation.trip_destination }}</h5>
                <p class="card-text">From: {{ reservation.trip_debut }} To: {{ reservation.trip_fin }}</p>
                <p class="card-text">Price: ${{ reservation.price }}</p>
                

                
              </div>
            </div>
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
      reservations: [],
    };
  },
  computed: {
    isAuthenticated() {
      return localStorage.getItem('auth_token') ? true : false;
    },
  },
  created() {
    if (this.isAuthenticated) {
      this.fetchReservations();
    }
  },
  methods: {
    async fetchReservations() {
      const token = localStorage.getItem('auth_token');
      try {
        const response = await fetch('http://127.0.0.1:8000/api/reservations/', {
          headers: {
            'Authorization': `Bearer ${token}`,
          },
        });

        if (response.ok) {
          this.reservations = await response.json();
        } else {
          console.error('Failed to fetch reservations');
        }
      } catch (error) {
        console.error('Error fetching reservations:', error);
      }
    },
    getTripImage(index) {
      // Custom logic to fetch the trip image based on index or any other criteria
      if (index === 0) return '/torre-eiffel-altura.avif';
      if (index === 1) return '/Times-Square-New-York-City.webp';
      return '/images (4).avif';
    },
  },
};
</script>

<style scoped>
.card {
  height: 100%;
}

.card-img-top {
  height: 200px;
  object-fit: cover;
}

.spinner-border {
  width: 3rem;
  height: 3rem;
}
</style>
