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

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator';
  import HelloWorld from '@/components/Accounts.vue'; // @ is an alias to /src

  @Component({
    components: {
      HelloWorld,
    },
  })
  export default class Home extends Vue {
  }
</script>
