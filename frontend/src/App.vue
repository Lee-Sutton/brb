<template>
  <div id="app">
    <div id="nav">
      <Navbar></Navbar>
    </div>
    <SideNav></SideNav>
    <div class="container" style="margin-top: 5%">
      <router-view/>
    </div>
  </div>
</template>

<script>
  import Navbar from '@/components/Navbar.vue';
  import SideNav from '@/components/SideNav.vue';

  export default {
    components: {
      Navbar,
      SideNav,
    },
  }

</script>

