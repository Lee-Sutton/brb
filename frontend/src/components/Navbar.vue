<template>
  <div>
    <b-navbar class="navbar navbar-expand-lg navbar-light bg-light" variant="info">
      <b-navbar-brand href="#">Golf Buddy</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <!--FIXME replace this with a helper function-->
        <template v-if="$store.state.isLoggedIn">
          <b-navbar-nav>
            <b-nav-item to="scores">Scores</b-nav-item>
          </b-navbar-nav>
        </template>
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
          </b-nav-form>

          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template slot="button-content"><em>User</em></template>
            <b-dropdown-item href="#">Profile</b-dropdown-item>
            <b-dropdown-item href="#">Sign Out</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
  export default {
    name: 'navbar'
  }
</script>
