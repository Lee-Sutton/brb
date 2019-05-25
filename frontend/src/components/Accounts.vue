<template>
    <div>
        <b-form @submit.prevent="onSubmit" id="account-form">
            <b-form-group label="Email address:" label-for="id_email"
                          description="We'll never share your email with anyone else.">
                <b-form-input id="id_email" v-model="form.email" type="email" required
                              placeholder="Enter email"></b-form-input>
            </b-form-group>

            <b-form-group label="Username:" label-for="id_username">
                <b-form-input id="id_username" v-model="form.username" required
                              placeholder="Enter username"></b-form-input>
            </b-form-group>

            <b-form-group label="Password" label-for="id_password">
                <b-form-input id="id_password" v-model="form.password1" type="password" required placeholder="Password"></b-form-input>
            </b-form-group>

            <b-form-group label="Confirm Password" label-for="id_password_confirm">
                <b-form-input id="id_password_confirm" v-model="form.password2" type="password" required
                              placeholder="Confirm Password"
                ></b-form-input>
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
            username: '',
            email: '',
            password1: '',
            password2: '',
        };

        async onSubmit() {
            await this.$store.dispatch('signup', this.form);
            await this.$router.push('/');
        }
    }
</script>

