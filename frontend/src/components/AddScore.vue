<template>
  <div>
    <b-form @submit.prevent="onSubmit" id="account-form">
      <b-form-group label="Score" label-for="id_score">
        <b-form-input id="id_score" v-model="doc.score" type="number" required
                      placeholder="Enter your final score"></b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
    </b-form>
  </div>
</template>


<script>
  import Score from '../models/score';

  export default {
    props: {
      id: {
        default: () => null
      }
    },

    data() {
      return {
        doc: this.id ? Score.find(this.id) : new Score()
      };
    },

    methods: {
      async onSubmit() {

        if (!this.doc.id) {
          await Score.$create(this.doc);
        } else {
          await Score.$update(this.doc);
        }
        this.$router.push({name: 'scores'});
      }
    }
  };

</script>

