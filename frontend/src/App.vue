<template>
  <div id="app">
    <div id="nav">
      <Navbar></Navbar>
    </div>
    <div class="container" style="margin-top: 5%">
      <router-view/>
    </div>
  </div>
</template>

<script>
  import Navbar from '@/components/Navbar.vue';

  export default {
    components: {
      Navbar,
    },
  }

</script>

