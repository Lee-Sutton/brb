import axios from 'axios';
import {HOST_URL} from "@/api/users";
import {Model} from '@vuex-orm/core'

export default class Score extends Model {
    static entity = 'scores';

    static fields() {
        return {
            id: this.number(0),
            score: this.number(0),
            slope: this.number(0),
            rating: this.number(0),
            // assignee: this.belongsTo(User, 'userId')
        }
    }

    get scoreRelativeToPar () {
        return this.score - this.rating;
    }

    static async $fetch () {
        const result = await axios.get(`${HOST_URL}/api/v1/${Score.entity}`);
        console.log(result);
        return this.insert(result);
    }
}
