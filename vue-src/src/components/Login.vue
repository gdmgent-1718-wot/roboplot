<template>
<div class="login">
    <div class="container">
        <div class="panel-body">
            <div class="col-lg-12">
                <form @submit.prevent="validateBeforeSubmit"> 
                    <div class="form-group">
                        <div class="control">
                            <input v-model="email" name="email" v-validate:email="'required|email'" :class="{'is-danger': errors.has('email') }" class="form-control" type="email" placeholder="email">
                        </div>
                        <p class="rood" v-if="errors.has('email')">{{ errors.first('email') }}</p>                
                    </div>
                    <div class="form-group">
                        <input v-model="password" name="password" type="password" id="password" v-validate:password="'required'" :class="{'is-danger': errors.has('password') }" class="form-control" placeholder="Password">
                        <p class="rood" v-if="errors.has('password')">{{ errors.first('password') }}</p>
                    </div>
                    <div class="form-group">
                        <div class="row">
                            <div class="col-sm-12">
                                <button name="login-submit" id="login-submit" class="form-control btn btn-login" value="Log In">Login</button>
                            </div>
                        </div>
                    </div>
                    <div class="form-group">
                        <div class="row">
                            <div class="col-sm-12 center">
                                <a v-on:click="register" name="register" class="links">Register</a>
                            </div>
                        </div>
                    </div>
                </form>
                <div v-if="errorslogin.length !== 0" class="alert alert-danger" role="alert">
                   <p v-for="errors in errorslogin">{{ errors }}</p>
                </div>
            </div>
        </div>
    </div>
</div>
</template>
<script>
/* eslint-disable */
import Vue from 'vue'
import VeeValidate from 'vee-validate'
import firebase from 'firebase'
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
  name: 'Login',
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
    validateBeforeSubmit: function(e) {
      this.$validator.validateAll()
      if (!this.errors.any()) {
        this.login()
      }
    },
    login: function(){
        this.errorslogin = []
        firebase.auth().signInWithEmailAndPassword(this.email, this.password).then(
            () => {
               this.$router.replace('home')
            },
            (err) => {             
                console.log('niet gelukt message: ' + err.message)
                this.errorslogin.push(err.message)
            }
        )
    },
    register: function(){
        this.$router.push('/registreer')
    }
  }
}
</script>
