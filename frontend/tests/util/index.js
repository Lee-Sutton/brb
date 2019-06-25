import Vue from 'vue'
import Vuex from 'vuex'
import VuexORM from '@vuex-orm/core';
import {createLocalVue} from '@vue/test-utils'
import {Database} from '@vuex-orm/core'

export const vue = createLocalVue();
vue.use(Vuex);

/**
 * Create a new Vuex Store.
 */
export function createStore(models) {
  const database = new Database();

  models.forEach((model) => {
    database.register(model, {})
  });

  const store = new Vuex.Store({
    plugins: [VuexORM.install(database)],
    strict: true
  });
};
