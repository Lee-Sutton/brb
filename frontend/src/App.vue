<template>
  <div class="d-flex toggle" id="wrapper">

    <!-- Sidebar -->
    <div class="bg-light border-right" id="sidebar-wrapper">
      <div class="sidebar-heading">Golf Buddy</div>
      <div class="list-group list-group-flush">
        <router-link to="scores" class="list-group-item list-group-item-action bg-light">Scores</router-link>
        <a href="#" class="list-group-item list-group-item-action bg-light">Drills</a>
        <a href="#" class="list-group-item list-group-item-action bg-light">Handicap</a>
        <a href="#" class="list-group-item list-group-item-action bg-light">Short Game</a>
        <a href="#" class="list-group-item list-group-item-action bg-light">Long Game</a>
        <a href="#" class="list-group-item list-group-item-action bg-light">Courses</a>
        <a href="#" class="list-group-item list-group-item-action bg-light">Find Friends</a>
      </div>
    </div>
    <!-- /#sidebar-wrapper -->

    <!-- Page Content -->
    <div id="page-content-wrapper">
      <Navbar></Navbar>

      <div class="container" id="router-view">
        <router-view></router-view>
      </div>

    </div>
    <!-- /#page-content-wrapper -->

  </div>
  <!-- /#wrapper -->
</template>

<!-- Bootstrap core JavaScript -->
<!-- Menu Toggle Script -->
<script>
  import Navbar from '@/components/Navbar'
  export default {
    components: {Navbar},
    name: 'App'
  }
</script>

<style scoped>
  body {
    overflow-x: hidden;
  }

  #router-view {
    margin-top: 5%;
  }

  #sidebar-wrapper {
    min-height: 100vh;
    margin-left: -15rem;
    -webkit-transition: margin .25s ease-out;
    -moz-transition: margin .25s ease-out;
    -o-transition: margin .25s ease-out;
    transition: margin .25s ease-out;
  }

  #sidebar-wrapper .sidebar-heading {
    padding: 0.875rem 1.25rem;
    font-size: 1.2rem;
  }

  #sidebar-wrapper .list-group {
    width: 15rem;
  }

  #page-content-wrapper {
    min-width: 100vw;
  }

  #wrapper.toggled #sidebar-wrapper {
    margin-left: 0;
  }

  @media (min-width: 768px) {
    #sidebar-wrapper {
      margin-left: 0;
    }

    #page-content-wrapper {
      min-width: 0;
      width: 100%;
    }

    #wrapper.toggled #sidebar-wrapper {
      margin-left: -15rem;
    }
  }
</style>
