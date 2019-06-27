<template>
  <div>
    <b-navbar class="navbar navbar-expand-lg navbar-light bg-light" variant="info">
      <h2>{{navbarRoute}}</h2>

      <b-collapse id="nav-collapse" is-nav>
        <!--FIXME replace this with a helper function-->
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">

          <template v-if="$store.state.isLoggedIn">
            <b-nav-form>
              <b-nav-item>
                <b-form-input size="sm" class="mr-sm-2" placeholder="Find a course"></b-form-input>
              </b-nav-item>
            </b-nav-form>

            <b-navbar-nav>
              <b-nav-item to="scores">Add Score</b-nav-item>
              <b-nav-item to="scores">Handicap</b-nav-item>
            </b-navbar-nav>
            <b-nav-item-dropdown right>
              <!-- Using 'button-content' slot -->
              <template slot="button-content"><em>User</em></template>
              <b-dropdown-item href="#">Profile</b-dropdown-item>
              <b-dropdown-item href="#">Sign Out</b-dropdown-item>
            </b-nav-item-dropdown>

          </template>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
  export default {
    name: 'navbar',
    computed: {
      navbarRoute () {
        return this.$route.meta.title;
      }
    }
  }
</script>
