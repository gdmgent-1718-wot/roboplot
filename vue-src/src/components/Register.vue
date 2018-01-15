<template>
<div class="login">
    <div class="container">
        <div class="panel-body">
        <form @submit.prevent="validateBeforeSubmit">
            <div class="col-lg-12">
                <div class="form-group">
                    <input v-model="email" name="email" v-validate:email="'required|email'" :class="{'is-danger': errors.has('email') }" class="form-control" type="text" placeholder="email">
                    <p class="rood" v-if="errors.has('email')">{{ errors.first('email') }}</p> 
                 </div>
                 <div class="form-group">
                    <input v-model="password" v-validate:password="'required'" type="password" name="password" :class="{'is-danger': errors.has('password')}" id="password"  class="form-control" placeholder="Password">
                    <p class="rood" v-if="errors.has('password')">{{ errors.first('password') }}</p>
                 </div>
                 <div class="form-group">
                    <input  v-validate="'required|confirmed:password'" type="password" name="confirm" :class="{'is-danger': errors.has('confirm')}" id="confirm"  class="form-control" placeholder="Confirm Password">
                    <p class="rood" v-if="errors.has('confirm')">{{ errors.first('confirm') }}</p>
                 </div>
                 <div class="form-group">
                     <div class="row">
                         <div class="col-sm-12">
                            <button  name="register" id="login-submit" class="form-control btn btn-login" value="Register">Register</button>
                         </div>
                     </div>
                 </div>
                <div class="form-group">
                    <div class="row">
                        <div class="col-sm-12 center">
                            <a class="links" v-on:click="login" name="login-submit">Login</a>
                        </div>
                    </div>
                </div>
            </div>
        </form>
        </div>
        <div v-if="errorslogin.length !== 0" class="alert alert-danger" role="alert">
            <p v-for="errors in errorslogin">{{ errors }}</p>
        </div>
    </div>
</div>
</template>
<script>
/* eslint-disable */
import Vue from 'vue'
import firebase from 'firebase'
import VeeValidate from 'vee-validate'
const msg = require('vee-validate/dist/locale/nl');
// nederlandse messages
Vue.use(VeeValidate, {
  locale: 'nl',
  dictionary: {
        nl: {
            messages: msg.default
        }
    }
  });
export default {
  name: 'Register',
  data () {
    return {
        errorslogin: [],
        email: null,
        password: null
    }
  },
  created () {
  },
  methods: {
    validateBeforeSubmit (e) {
      this.$validator.validateAll()
      if (!this.errors.any() && this.email != null && this.password != null) {
        this.registreer()
      }
    },
    login: function(){
        this.$router.push('/login')
    },
    registreer: function(){
        this.errorslogin = []
        firebase.auth().createUserWithEmailAndPassword(this.email, this.password).then(
            (user) => {
                console.log('aangemaakt')
                 this.$router.replace('home')
            },
            (err) => {
                console.log('niet gelukt message: ' + err.message)
                this.errorslogin.push(err.message)
            }
        )
    },

  }
}
</script>
