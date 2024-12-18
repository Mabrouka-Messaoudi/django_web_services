<template>
  <div class="admin-panel mt-5">
    <h2 class="text-center mb-3">Admin Panel</h2>
    <!-- Formulaire pour Ajouter/Modifier un Voyage -->
    <form @submit.prevent="saveTrip">
      <div class="row mb-3">
        <div class="col-md-3">
          <input v-model="currentTrip.destination" type="text" class="form-control" placeholder="Destination" />
        </div>
        <div class="col-md-2">
          <input v-model="currentTrip.debut" type="date" class="form-control" placeholder="Start Date" />
        </div>
        <div class="col-md-2">
          <input v-model="currentTrip.fin" type="date" class="form-control" placeholder="End Date" />
        </div>
        <div class="col-md-2">
          <input v-model="currentTrip.prix" type="number" class="form-control" placeholder="Price" />
        </div>
        <div class="col-md-2">
          <input v-model="currentTrip.image" type="text" class="form-control" placeholder="Image URL" />
        </div>
        <div class="col-md-1">
          <button class="btn btn-success w-100" type="submit">
            {{ currentTrip.id ? "Update" : "Add" }}
          </button>
        </div>
      </div>
    </form>

    <!-- Liste des voyages -->
    <div v-for="trip in trips" :key="trip.id" class="admin-trip-item mb-3 d-flex align-items-center">
      <span>{{ trip.destination }} ({{ trip.debut }} to {{ trip.fin }}, ${{ trip.prix }})</span>
      <button class="btn btn-warning btn-sm mx-2" @click="editTrip(trip)">Edit</button>
      <button class="btn btn-danger btn-sm" @click="deleteTrip(trip.id)">Delete</button>
    </div>
  </div>
</template>

<script>
export default {
  props: ["trips"], // Recevoir la liste des voyages en props
  data() {
    return {
      currentTrip: {
        id: null,
        destination: "",
        debut: "",
        fin: "",
        prix: "",
        image: "",
      },
    };
  },
  methods: {
    saveTrip() {
      this.$emit("save-trip", this.currentTrip);
      this.resetForm();
    },
    editTrip(trip) {
      this.currentTrip = { ...trip };
    },
    deleteTrip(id) {
      this.$emit("delete-trip", id);
    },
    resetForm() {
      this.currentTrip = { id: null, destination: "", debut: "", fin: "", prix: "", image: "" };
    },
  },
};
</script>

<style scoped>
.admin-panel {
  background-color: #f8f9fa;
  padding: 20px;
  border-radius: 5px;
}
</style>

