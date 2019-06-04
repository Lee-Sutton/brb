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


<script lang="ts">
    import {Component, Prop, Vue} from 'vue-property-decorator';
    import Score from '../models/score';

    @Component
    export default class AddScore extends Vue {
        // TODO Replace with deep copy
        doc = {
            score: null,
        };

        async onSubmit() {
            const score = new Score(this.doc);
            console.log(score);

            if (!score.id) {
                await Score.$create(score);
            } else {
                await Score.$update(score);
            }
            this.$router.push({name: 'scores'});
        }
    }
</script>

