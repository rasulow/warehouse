import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import axios from 'axios'
import BASE_URL from "@/utils/url";
// import is_have from './utils/haveToken'



Vue.config.productionTip = false

axios.defaults.baseURL = BASE_URL

const token = 'Bearer ' + localStorage.getItem('token')
axios.defaults.headers['Authorization'] = token


new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')

