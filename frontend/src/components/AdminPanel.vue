<template>
  <div class="container my-5">
    <h1 class="text-center mb-4">Available Trips</h1>

    <!-- Add Trip Form -->
    <div v-if="isAuthenticated" class="mb-4">
      <button class="btn btn-success mb-3" @click="toggleAddTripForm">
  {{ showAddTripForm ? (newTrip.id ? 'Save Changes' : 'Cancel Add Trip') : (newTrip.id ? 'Edit Trip' : 'Add Trip') }}
</button>


      <div v-if="showAddTripForm">
        <h3 class="text-center">Add a New Trip</h3>
        <form @submit.prevent="addTrip" class="mt-3">
          <div class="row g-3">
            <div class="col-md-4">
              <input
                type="text"
                class="form-control"
                placeholder="Destination"
                v-model="newTrip.destination"
                required
              />
            </div>
            <div class="col-md-4">
              <input
                type="date"
                class="form-control"
                placeholder="Start Date"
                v-model="newTrip.debut"
                required
              />
            </div>
            <div class="col-md-4">
              <input
                type="date"
                class="form-control"
                placeholder="End Date"
                v-model="newTrip.fin"
                required
              />
            </div>
            <div class="col-md-4 mt-3">
              <input
                type="number"
                class="form-control"
                placeholder="Price"
                v-model="newTrip.prix"
                required
              />
            </div>
            <div class="col-md-4 mt-3">
              <button type="submit" class="btn btn-success w-100">
                Add Trip
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>

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
        <div v-if="trip" class="card shadow-sm">
          <img :src="getTripImage(index)" class="card-img-top" alt="Trip image" />
          <div class="card-body">
            <h5 class="card-title">{{ trip.destination }}</h5>
            <p class="card-text">From: {{ trip.debut }} To: {{ trip.fin }}</p>
            <p class="card-text">Price: ${{ trip.prix }}</p>

            <button v-if="isAuthenticated" class="btn btn-primary" @click="openCreateReservationForm(trip)">
              Reserve Now
            </button>

            <p v-else class="mt-3">
              Please <a href="/login" class="btn btn-link">Login</a> to create a reservation.
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

    <!-- Create Reservation Form -->
    <div v-if="currentTrip" class="mt-5">
      <h2 class="text-center">Create Reservation</h2>

      <form @submit.prevent="submitReservation" class="mt-3">
        <div class="row g-3">
          <div class="col-md-6">
            <input
              type="date"
              class="form-control"
              placeholder="Reservation Date"
              v-model="reservationDate"
              required
            />
          </div>
          <div class="col-md-6">
            <input
              type="number"
              class="form-control"
              placeholder="Number of Guests"
              v-model="numGuests"
              required
            />
          </div>
          <div class="col-md-12 mt-3">
            <button type="submit" class="btn btn-success w-100">
              Create Reservation
            </button>
          </div>
        </div>
      </form>
    </div>

    <!-- Manage Clients -->
    <div class="mt-5">
      <h2 class="text-center">Manage Clients</h2>

      <!-- Client List -->
      <ul class="list-group my-4">
        <li v-for="client in clients" :key="client.id" class="list-group-item d-flex justify-content-between align-items-center">
          <span>{{ client.username }} - {{ client.nom }} {{ client.prenom }} ({{ client.email }})</span>
          <span>
            <button class="btn btn-warning btn-sm me-2" @click="editClient(client)">Edit</button>
            <button class="btn btn-danger btn-sm" @click="deleteClient(client.id)">Delete</button>
          </span>
        </li>
      </ul>

      <!-- Add/Edit Client Form -->
      <form @submit.prevent="saveClient" class="mt-3">
        <div class="row g-3">
          <div class="col-md-3">
            <input
              type="text"
              class="form-control"
              placeholder="Username"
              v-model="currentClient.username"
              required
            />
          </div>
          <div class="col-md-3">
            <input
              type="text"
              class="form-control"
              placeholder="First Name"
              v-model="currentClient.nom"
            />
          </div>
          <div class="col-md-3">
            <input
              type="text"
              class="form-control"
              placeholder="Last Name"
              v-model="currentClient.prenom"
            />
          </div>
          <div class="col-md-3">
            <input
              type="text"
              class="form-control"
              placeholder="Phone"
              v-model="currentClient.num_tel"
            />
          </div>
          <div class="col-md-4 mt-3">
            <input
              type="email"
              class="form-control"
              placeholder="Email"
              v-model="currentClient.email"
              required
            />
          </div>
          <div class="col-md-4 mt-3">
            <button type="submit" class="btn btn-success w-100">
              {{ currentClient.id ? "Update Client" : "Add Client" }}
            </button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

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
      clients: [],
      currentClient: {
        id: null,
        username: "",
        nom: "",
        prenom: "",
        num_tel: "",
        email: "",
      },
      currentTrip: null,
      reservationDate: "",
      numGuests: 1,
      showAddTripForm: false, // Toggle visibility of Add Trip form
      newTrip: {
        destination: "",
        debut: "",
        fin: "",
        prix: "",
      },
    };
  },
  computed: {
    isAuthenticated() {
      return localStorage.getItem("auth_token") ? true : false;
    },
    filteredTrips() {
      return this.trips.filter((trip) => {
        if (!trip) return false; // Ensure trip is not null or undefined
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
    this.fetchClients();
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
    async fetchClients() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/clients/");
        this.clients = response.data;
      } catch (error) {
        console.error("Error fetching clients:", error);
      }
    },
    openCreateReservationForm(trip) {
      this.currentTrip = trip;
    },
    editTrip(trip) {
  // Prefill the form with the selected trip's details
  this.newTrip = { ...trip };
  this.showAddTripForm = true; // Show the Add Trip form in edit mode
},
async deleteTrip(tripId) {
  const authToken = localStorage.getItem("auth_token");
  if (!authToken) {
    alert("Please login to delete a trip.");
    return;
  }

  try {
    const response = await axios.delete(`http://127.0.0.1:8000/voyages/${tripId}/`, {
      headers: {
        Authorization: `Bearer ${authToken}`,
      },
    });

    if (response.status === 204) {
      alert("Trip deleted successfully!");
      // Remove the deleted trip from the trips array
      this.trips = this.trips.filter((trip) => trip.id !== tripId);
    } else {
      alert("Failed to delete the trip. Please try again.");
    }
  } catch (error) {
    console.error("Error deleting trip:", error);
    alert("Error deleting trip. Please try again.");
  }
},


    async submitReservation() {
      try {
        const authToken = localStorage.getItem("auth_token");
        if (!authToken) {
          alert("Please login to create a reservation.");
          return;
        }

        const reservationData = {
          trip_id: this.currentTrip.id,
          reservation_date: this.reservationDate,
          num_guests: this.numGuests,
        };

        const response = await fetch("http://127.0.0.1:8000/reservation/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${authToken}`,
          },
          body: JSON.stringify(reservationData),
        });

        if (response.ok) {
          alert("Reservation created successfully!");
          this.resetReservationForm();
        } else {
          const errorData = await response.json();
          alert(`Failed to create reservation: ${errorData.message}`);
        }
      } catch (error) {
        console.error("Error creating reservation:", error);
        alert("Error creating reservation. Please try again.");
      }
    },
    resetReservationForm() {
      this.currentTrip = null;
      this.reservationDate = "";
      this.numGuests = 1;
    },
    editClient(client) {
      this.currentClient = { ...client };
    },
    async saveClient() {
      try {
        if (this.currentClient.id) {
          await axios.put(
            `http://127.0.0.1:8000/client/${this.currentClient.id}/`,
            this.currentClient
          );
        } else {
          await axios.post("http://127.0.0.1:8000/clients/", this.currentClient);
        }
        this.resetClientForm();
        this.fetchClients();
      } catch (error) {
        console.error("Error saving client:", error);
      }
    },
    async deleteClient(clientId) {
      try {
        await axios.delete(`http://127.0.0.1:8000/client/${clientId}/`);
        this.fetchClients();
      } catch (error) {
        console.error("Error deleting client:", error);
      }
    },
    resetClientForm() {
      this.currentClient = {
        id: null,
        username: "",
        nom: "",
        prenom: "",
        num_tel: "",
        email: "",
      };
    },
    getTripImage(index) {
      if (index === 0) return "/torre-eiffel-altura.avif";
      if (index === 1) return "/Times-Square-New-York-City.webp";
      return "/i1.jpeg";
    },
    async addTrip() {
      const authToken = localStorage.getItem("auth_token");
      if (!authToken) {
        alert("Please login to add a trip.");
        return;
      }

      try {
        const response = await axios.post("http://127.0.0.1:8000/voyages/", this.newTrip, {
          
        });

        if (response.data) {
          alert("Trip added successfully!");
          this.trips.push(response.data);
          this.showAddTripForm = false;
          this.newTrip = {
            destination: "",
            debut: "",
            fin: "",
            prix: "",
          };
        }
      } catch (error) {
        console.error("Error adding trip:", error);
        alert("Failed to add trip. Please try again.");
      }
    },
  },
};
</script>

<style>
.container {
  max-width: 1200px;
}
</style>
