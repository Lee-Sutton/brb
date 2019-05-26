<template>
    <div>
        <b-row>
            <b-col md="4">
                <h2>My Scores</h2>
            </b-col>

            <b-col md="4" offset-md="4">
                <button class="btn btn-primary float-right">Add Score</button>
            </b-col>
        </b-row>
        <div class="row">
            <b-table striped hover :items="items"></b-table>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                items: [
                    {age: 40, first_name: 'Dickerson', last_name: 'Macdonald'},
                    {age: 21, first_name: 'Larsen', last_name: 'Shaw'},
                    {age: 89, first_name: 'Geneva', last_name: 'Wilson'},
                    {age: 38, first_name: 'Jami', last_name: 'Carney'}
                ]
            }
        }
    }
</script>
