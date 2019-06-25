import axios from 'axios';
import {HOST_URL} from "@/api/users";
import {Model} from '@vuex-orm/core'
import AxiosModel from './axios-model'

export default class Score extends AxiosModel {
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
}
