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

    static async $fetch () {
        const result = await axios.get(`${HOST_URL}/api/v1/${this.entity}`);
        return this.insert(result);
    }
    static async $create ({data}) {
        const doc = new Score(data);
        // TODO if it fails, remove the document from the store and display the error
        // TODO Optimistic ui
        return await axios.post(`${HOST_URL}/api/v1/${this.entity}`, doc);
    }
}
