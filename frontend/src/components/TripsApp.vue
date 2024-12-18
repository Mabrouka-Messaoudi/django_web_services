<template>
  <div class="container my-5">
    <h1 class="text-center mb-4">Available Trips</h1>

    <!-- Search Section -->
    <div class="mb-4">
      <div class="row">
        <div class="col-md-3">
          <input
            type="text"
            class="form-control"
            placeholder="Search by Destination"
            v-model="search.destination"
          />
        </div>
        <div class="col-md-3">
          <input
            type="date"
            class="form-control"
            placeholder="Start Date"
            v-model="search.startDate"
          />
        </div>
        <div class="col-md-3">
          <input
            type="date"
            class="form-control"
            placeholder="End Date"
            v-model="search.endDate"
          />
        </div>
        <div class="col-md-3">
          <input
            type="number"
            class="form-control"
            placeholder="Max Price"
            v-model="search.maxPrice"
          />
        </div>
      </div>
    </div>

    <!-- No Trips Available -->
    <div v-if="filteredTrips.length === 0" class="alert alert-warning text-center">
      No trips available.
    </div>

    <!-- Trips List -->
    <div class="row">
      <div v-for="(trip, index) in filteredTrips" :key="trip.id" class="col-md-4 mb-4">
        <div class="card shadow-sm">
          <img :src="getTripImage(index)" class="card-img-top" alt="Trip image" />
          <div class="card-body">
            <h5 class="card-title">{{ trip.destination }}</h5>
            <p class="card-text">From: {{ trip.debut }} To: {{ trip.fin }}</p>
            <p class="card-text">Price: ${{ trip.prix }}</p>

            <button v-if="isAuthenticated" class="btn btn-primary" @click="reserveTrip(trip.id)">
              Reserve Now
            </button>

            <p v-else class="mt-3">
              Please <a href="/login" class="btn btn-link">Login</a> to reserve.
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- Loading Spinner -->
    <div v-if="isLoading" class="text-center">
      <div class="spinner-border" role="status">
        <span class="sr-only">Loading...</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      trips: [],
      isLoading: false,
      search: {
        destination: "",
        startDate: "",
        endDate: "",
        maxPrice: "",
      },
    };
  },
  computed: {
    isAuthenticated() {
      return localStorage.getItem("auth_token") ? true : false;
    },
    filteredTrips() {
      return this.trips.filter((trip) => {
        const matchesDestination =
          this.search.destination === "" ||
          trip.destination.toLowerCase().includes(this.search.destination.toLowerCase());
        const matchesStartDate =
          this.search.startDate === "" ||
          new Date(trip.debut) >= new Date(this.search.startDate);
        const matchesEndDate =
          this.search.endDate === "" ||
          new Date(trip.fin) <= new Date(this.search.endDate);
        const matchesMaxPrice =
          this.search.maxPrice === "" || trip.prix <= parseFloat(this.search.maxPrice);

        return matchesDestination && matchesStartDate && matchesEndDate && matchesMaxPrice;
      });
    },
  },
  created() {
    this.fetchTrips();
  },
  methods: {
    async fetchTrips() {
      this.isLoading = true;
      try {
        const response = await fetch("http://127.0.0.1:8000/voyages/");
        if (response.ok) {
          this.trips = await response.json();
        } else {
          alert("Failed to load trips. Please try again.");
        }
      } catch (error) {
        alert("Error loading trips. Please check your connection.");
      } finally {
        this.isLoading = false;
      }
    },
    getTripImage(index) {
      if (index === 0) return "/torre-eiffel-altura.avif";
      if (index === 1) return "/Times-Square-New-York-City.webp";
      return "/i1.jpeg";
    },
    async reserveTrip(tripId) {
      try {
        const authToken = localStorage.getItem("auth_token");
        if (!authToken) {
          alert("Please login to reserve a trip.");
          return;
        }

        const response = await fetch("http://127.0.0.1:8000/reservation/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${authToken}`,
          },
          body: JSON.stringify({ voyage_id: tripId }),
        });

        if (response.ok) {
          const reservationData = await response.json();
          alert("Trip reserved successfully!");
          this.$router.push({ name: "ReservationDetails", params: { id: reservationData.reservation.id } });
        } else {
          const errorData = await response.json();
          alert(`Failed to reserve trip: ${errorData.error || "Unknown error"}`);
        }
      } catch (error) {
        console.error("Error reserving trip:", error);
        alert("An error occurred while reserving the trip. Please try again.");
      }
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
