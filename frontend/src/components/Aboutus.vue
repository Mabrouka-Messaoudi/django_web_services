<template>
  <div>
    <!-- Header Section -->
    <header>
      <div class="header-content">
        <h1>About Us</h1>
      </div>
    </header>

    <!-- Main Content -->
    <main>
      <!-- Section with 3 Icons and Descriptions -->
      <section class="features">
        <div class="feature">
          <img src="@/assets/team.png" alt="About us" />
          <h3>Great team work</h3>
          <p>Our team at Safrati is a dedicated group of passionate travel experts who work together to create exceptional experiences for our clients. Through collaboration, creativity, and a shared commitment to excellence, we ensure that every trip is executed flawlessly.</p>
        </div>
        <div class="feature">
          <img src="@/assets/vision-icon.png" alt="Our vision" />
          <h3>Our vision</h3>
          <p>At Safrati, our vision is to provide unforgettable travel experiences that inspire adventure and create lasting memories. We aim to offer unique destinations, personalized services, and seamless journeys that meet the desires of every traveler.</p>
        </div>
        <div class="feature">
          <img src="@/assets/ourmission.png" alt="Our mission" />
          <h3>Our mission</h3>
          <p>Safrati's mission is to offer top-quality travel services, focusing on customer satisfaction, reliability, and sustainability. We strive to make travel accessible and enjoyable for everyone, while supporting the local communities we visit, ensuring a positive impact on both our clients and the destinations. </p>
          
        </div>
      </section>
    </main>

    <!-- Footer -->
    <footer>
    <P>
    <h2>Contact us<br></h2>
      hamzazarai11@gmail.com<br>mabroukamessaoudi892@gmail.com
    </p>
      <p>&copy; Safrati 2024</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: "AboutUs",
};
</script>

<style scoped>
/* Header Styling */
header {
  background: url('@/assets/aboutus.jpg') no-repeat center center/cover;
  color: white;
  text-align: center;
  padding: 380px 80px;
}

header .header-content h1 {
  font-size: 3rem;
  margin-bottom: 10px;
}

/* Features Section */
.features {
  display: flex;
  justify-content: space-around;
  margin: 50px 0;
  text-align: center;
}

.feature {
  background-color: #fff;
  border: 1px solid #ddd;
  padding: 20px;
  width: 30%;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.feature img {
  width: 80px;
  margin: 0 auto 15px; /* Centrage de l'image */
  display: block; /* Assurez-vous que l'image est centrée */
}

/* Testimonial Section */
.testimonial {
  background-color: #fff;
  padding: 50px 20px;
  margin: 50px 0;
}

.testimonial-content {
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.testimonial-content img {
  width: 120px;
  border-radius: 50%;
  margin-right: 30px;
}

/* Footer Styling */
footer {
  background-color: #333;
  color: white;
  text-align: center;
  padding: 20px;
}

footer p {
  font-size: 1rem;
}

/* Reset default styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
  color: #333;
}
</style>
