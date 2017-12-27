// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueFire from 'vuefire'
import App from './App'
import * as firebase from 'firebase'
import 'font-awesome/css/font-awesome.css'
import '@/assets/sass/main.scss'
require('../node_modules/bootstrap-sass/assets/stylesheets/_bootstrap.scss')
Vue.use(VueFire)
firebase.initializeApp({
  apiKey: 'AIzaSyCQlYBkHTw5Q6N6A7_ygs6w8OkrKPE44uY',
  authDomain: 'roboplot-1.firebaseapp.com',
  databaseURL: 'https://roboplot-1.firebaseio.com',
  projectId: 'roboplot-1',
  storageBucket: 'roboplot-1.appspot.com',
  messagingSenderId: '775004018292'
})
/* eslint-disable no-new */
new Vue({
  el: '#app',
  template: '<App/>',
  components: { App }
})
