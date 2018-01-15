// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
/* eslint-disable */
import Vue from 'vue'
import VueFire from 'vuefire'
import App from './App'
import router from './router'
import VueRouter from 'vue-router'
import SweetModal from 'sweet-modal-vue/src/plugin.js'
import VeeValidate from 'vee-validate'
import firebase from 'firebase'
import './assets/js/firebase'
import 'font-awesome/css/font-awesome.css'
import '@/assets/sass/main.scss'
require('../node_modules/bootstrap-sass/assets/stylesheets/_bootstrap.scss')
Vue.use(VueFire)
Vue.use(SweetModal)
Vue.use(VueRouter)
Vue.config.productionTip = false
let app;
firebase.auth().onAuthStateChanged(function(user){
  if(!app){
    new Vue({
      el: '#app',
      router,
      template: '<App/>',
      components: { App }
    })
  }
})


