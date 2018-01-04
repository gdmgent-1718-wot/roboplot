// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueFire from 'vuefire'
import App from './App'
import SweetModal from 'sweet-modal-vue/src/plugin.js'
import 'font-awesome/css/font-awesome.css'
import '@/assets/sass/main.scss'
require('../node_modules/bootstrap-sass/assets/stylesheets/_bootstrap.scss')
Vue.use(VueFire)
Vue.use(SweetModal)
/* eslint-disable no-new */
new Vue({
  el: '#app',
  template: '<App/>',
  components: { App }
})
