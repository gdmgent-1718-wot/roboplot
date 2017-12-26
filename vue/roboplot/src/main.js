// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueFire from 'vuefire'
import App from './App'
import 'font-awesome/css/font-awesome.css'
import '@/assets/js/main.js'
import '@/assets/sass/main.scss'
require('../node_modules/bootstrap-sass/assets/stylesheets/_bootstrap.scss')
Vue.use(VueFire)
/* eslint-disable no-new */
new Vue({
  el: '#app',
  template: '<App/>',
  components: { App }
})
