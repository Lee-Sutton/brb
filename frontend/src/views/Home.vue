<template>
  <div class="home">
    <div v-if="$store.state.isLoggedIn">
      <p>Welcome user</p>
    </div>
    <div v-else>
      <b-jumbotron header="Golf Buddy" lead="Welcome to Golf Buddy">
        <p>Create an account to get started</p>
        <router-link :to="{path: 'accounts'}" class="btn btn-primary" data-cy="sign-up">Sign up</router-link>
      </b-jumbotron>
    </div>
  </div>
</template>


<script>
  export default {
    name: 'home',
  };
</script>
