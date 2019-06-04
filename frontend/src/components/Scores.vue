<template>
  <div>
    <b-row>
      <b-col md="4">
        <h2>My Scores</h2>
      </b-col>

      <b-col md="4" offset-md="4">
        <router-link :to="{name: 'add-score'}" class="btn btn-primary float-right">Add Score</router-link>
      </b-col>
    </b-row>
    <div class="row">
      <b-table striped hover :items="allScoreCards" :fields="fields">
        <template slot="actions" slot-scope="line">
          <b-button-toolbar>
            <b-button-group class="mx-1">
              <b-button size="sm" variant="primary" @click="handleEdit(line)">
                Edit
              </b-button>
            </b-button-group>
            <b-button-group>
              <b-button size="sm" variant="danger" @click="handleRemove(line)">
                Remove
              </b-button>
            </b-button-group>
          </b-button-toolbar>
        </template>
      </b-table>
    </div>
  </div>
</template>

<script>

  import Score from '../models/score';

  export default {
    async mounted() {
      await Score.$fetch();
      this.allScoreCards = Score.all();
    },
    data() {
      return {
        allScoreCards: [],
        fields: [
          {
            key: 'score',
            sortable: true
          },
          {
            key: 'rating',
            sortable: true
          },
          {
            key: 'slope',
            sortable: true
          },
          {
            key: 'created',
            label: 'Shot at',
            sortable: true,
          },
          {
            key: 'actions',
          }
        ],
      }
    },
    methods: {
      handleRemove(line) {
        console.log('not implemented');
      },

      handleEdit(line) {
        this.$router.push({name: 'add-score', params: {id: line.item.id}})
      }
    }
  }
</script>
