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
            <b-table striped hover :items="allScoreCards" :fields="fields"></b-table>
        </div>
    </div>
</template>

<script>
    import gql from 'graphql-tag';

    export default {
        data() {
            return {
                allScoreCards: [],
                fields: [
                    {
                        key: 'score',
                        sortable: true
                    },
                    {
                        key: 'created',
                        label: 'Shot at',
                        sortable: true,
                    }
                ],
            }
        },
        apollo: {
            allScoreCards: gql`query { allScoreCards { score } }`
        }
    }
</script>
