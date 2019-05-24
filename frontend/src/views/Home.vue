<template>
    <div class="home">
        <b-jumbotron header="Golf Buddy" lead="Welcome to Golf Buddy" style="margin-top: 10%">
            <p>Create an account to get started</p>
            <router-link to="/" class="btn btn-primary">Sign up</router-link>
        </b-jumbotron>
    </div>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator';
  import HelloWorld from '@/components/HelloWorld.vue'; // @ is an alias to /src

  @Component({
    components: {
      HelloWorld,
    },
  })
  export default class Home extends Vue {
  }
</script>
