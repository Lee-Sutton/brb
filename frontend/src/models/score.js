import axios from 'axios';
import {HOST_URL} from "@/api/users";
import {Model} from '@vuex-orm/core'

export default class Score extends Model {
  static entity = 'scores';

  static fields() {
    return {
      id: this.attr(null),
      score: this.number(0),
      slope: this.number(0),
      rating: this.number(0),
      // TODO add this
      // assignee: this.belongsTo(User, 'userId')
    }
  }

  static async $fetch () {
    const result = await axios.get(`${HOST_URL}/api/v1/${this.entity}`);
    return this.insert(result);
  }

  static async $create (record) {
    // TODO Optimistic ui
    return await axios.post(`${HOST_URL}/api/v1/${this.entity}`, record.$toJson());
  }

  static async $update(record) {
    return await axios.put(`${HOST_URL}/api/v1/${this.entity}/${record.id}/`, record.$toJson());
  }
}
