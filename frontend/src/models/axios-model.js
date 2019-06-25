import axios from 'axios';
import {Model} from '@vuex-orm/core'

export const HOST_URL = 'http://localhost:8000';

export default class AxiosModel extends Model {
  /**
   * Fetches all relevant models from the api endpoint using a get request
   * Fetched documents are inserted into the store
   *  @return {Promise<Collections<InstanceOf<AxiosModel>>>}
   */
  static async $fetch () {
    const result = await axios.get(`${HOST_URL}/api/v1/${this.entity}`);
    return this.insert(result);
  }

  /**
   * Creates the record by making a post request to the api endpoint
   * @param record {Model}
   * @return {Promise<Collections<T>>}
   */
  static async $create (record) {
    // TODO Optimistic ui
    return axios.post(`${HOST_URL}/api/v1/${this.entity}`, record.$toJson());
  }

  /**
   * Updates the input record using a put request to the api endpoint
   * @param record {Model}
   * @return {Promise<AxiosResponse<T>>}
   */
  static async $update(record) {
    return await axios.put(`${HOST_URL}/api/v1/${this.entity}/${record.id}`, record.$toJson());
  }
}
