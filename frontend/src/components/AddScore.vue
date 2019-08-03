<template>
  <div>
    <b-form @submit.prevent="onSubmit" id="account-form">
      <b-form-group label="Score" label-for="id_score">

        <b-form-input id="id_score" v-model="doc.score" type="number" required
                      placeholder="Enter your final score"></b-form-input>
      </b-form-group>

      <b-form-group label="Slope" label-for="id_score">
        <b-form-input id="id_score" v-model="doc.slope" type="number" required
                      placeholder="Course slope"></b-form-input>
      </b-form-group>

      <b-form-group label="Rating" label-for="id_score">
        <b-form-input id="id_score" v-model="doc.rating" type="number" required
                      placeholder="Course rating"></b-form-input>
      </b-form-group>

      <b-button type="submit" variant="primary">Submit</b-button>
    </b-form>
  </div>
</template>


<script>
  import Score from '../models/score';

  export default {
    data() {
      return {
        doc: this.$router.id ? Score.find(this.id) : new Score()
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

