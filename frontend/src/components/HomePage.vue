<template>
  <div class="hero-section">
    <!-- Video Background -->
    <video autoplay muted loop class="video-background">
      <source src="@/assets/video.mp4" type="video/mp4" />
      Your browser does not support the video tag.
    </video>

    <!-- Content Overlay -->
    <div class="content-overlay">
      <h1>Make in <br /> your journey.</h1>
      <p>Explore the world with what you love, beautiful natural beauty.</p>
      
    </div>
  </div>
</template>

<script>
export default {
  name: "HomePage",
};
</script>

<style scoped>
/* Hero Section Styles */
.hero-section {
  position: relative;
  height: 100vh; /* Full viewport height */
  overflow: hidden;
}

/* Video Background */
.video-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover; /* Ensures the video covers the container */
  z-index: -1;
}

/* Content Overlay */
.content-overlay {
  position: relative;
  z-index: 1;
  text-align: center;
  color: #fff;
  margin-top: 15%;
}

.content-overlay h1 {
  font-size: 4rem;
  font-weight: bold;
  line-height: 1.2;
}

.content-overlay p {
  margin: 10px 0 20px;
  font-size: 1.2rem;
  color: #f4f4f4;
}

/* Search Bar */
.search-bar {
  display: flex;
  justify-content: center;
  gap: 10px;
}

.search-bar input,
.explore-btn {
  padding: 10px 15px;
  font-size: 1rem;
  border: none;
  border-radius: 5px;
}

.search-bar input {
  width: 200px;
}

.explore-btn {
  background-color: #000;
  color: #fff;
  cursor: pointer;
  transition: background-color 0.3s;
}

.explore-btn:hover {
  background-color: #00bcd4;
}
</style>
