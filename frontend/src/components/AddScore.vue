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
    import Score from '@/models/score'

    @Component
    export default class AddScore extends Vue {
        form = {
            score: null,
        };

        async onSubmit() {
            await Score.$create({
                data: this.form,
            });
            // await Score.$fetch({
            //     data: this.form,
            // });
            this.$router.push({name: 'scores'});
        }
    }
</script>

