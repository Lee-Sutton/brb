<template>
    <div>
        <b-form @submit.prevent="onSubmit" id="account-form">
            <b-form-group label="Score" label-for="id_score">
                <b-form-input id="id_score" v-model="form.score" type="number" required
                              placeholder="Enter your final score"></b-form-input>
            </b-form-group>
            <b-button type="submit" variant="primary">Submit</b-button>
        </b-form>
    </div>
</template>


<script lang="ts">
    import {Component, Vue} from 'vue-property-decorator';

    @Component
    export default class Accounts extends Vue {
        form = {
            score: null,
        };

        async onSubmit() {
            this.$apollo.mutate({
                mutation: gql
            });
        }

        addTag() {
            // We save the user input in case of an error
            // We clear it early to give the UI a snappy feel
            this.newTag = '';
            // Call to the graphql mutation
            this.$apollo.mutate({
                // Query
                mutation: gql`mutation ($label: String!) { addTag(label: $label) { id label } }`,
                // Parameters
                variables: {
                    label: newTag,
                },
            }).then((data) => {
                // Result
                console.log(data)
            }).catch((error) => {
                // Error
                console.error(error)
                // We restore the initial user input
                this.newTag = newTag
            })
        }

    ,
    }
</script>

