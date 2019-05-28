import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import './registerServiceWorker';
import ApolloClient from 'apollo-boost'
import VueApollo from 'vue-apollo'

const apolloClient = new ApolloClient({
    // TODO get this from the env file
    uri: 'http://localhost:8000/graphql/'
});

const apolloProvider = new VueApollo({
  defaultClient: apolloClient,
});

Vue.use(VueApollo);


Vue.use(BootstrapVue);

Vue.config.productionTip = false;

new Vue({
    router,
    store,
    apolloProvider,
    render: (h) => h(App),
}).$mount('#app');
