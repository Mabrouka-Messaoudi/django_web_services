<template>
  <div id="app">
    <NavbarBoot />
    <router-view /> <!-- Where the rest of your pages will be rendered -->
  </div>
</template>

<script>
import NavbarBoot from './components/NavbarBoot.vue';

export default {
  name: 'App',
  components: {
    NavbarBoot
  }
};
</script>
