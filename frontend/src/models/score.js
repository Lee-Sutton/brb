import axios from 'axios';
import {HOST_URL} from "@/api/users";
import {Model} from '@vuex-orm/core'
import AxiosModel from './axios-model'

export default class Score extends AxiosModel {
  static entity = 'scores';

  static fields() {
    return {
      id: this.attr(null),
      score: this.number(null),
      slope: this.number(null),
      rating: this.number(null),
      // TODO add this
      // assignee: this.belongsTo(User, 'userId')
    }
  }
}
