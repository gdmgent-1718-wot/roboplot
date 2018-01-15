<template>
  <div class="main">
    <div class="container">
      <div>
        <div class="content">
          <div class="card">
            <h3 class="left">Recorded paths</h3></h1>
            <ul class="list-group">
              <li class="list-group-item textleft" v-for="records in records" v-bind:class="{ act: records.actief }">
                <span class="badge badge-primary badge-pill">{{ records.datum }}</span>
                <span class="left">{{ records.naam }}</span>
                <a class="right actionbuttons" @click="toggle(records)" v-show="!records.actief"><i class="fa fa-trash fa-2x" aria-hidden="true"></i></a>
                <a class="right actionbuttons" @click="toevoegen(records)" v-show="!records.actief"><i class="fa fa-plus fa-2x" aria-hidden="true"></i></a>
                <a class="right actionbuttons" @click="verwijderen(records['.key'])" v-show="records.actief"><i class="fa fa-minus fa-2x" aria-hidden="true"></i></a>
              </li>
            </ul>
          </div>
          <div class="card" v-if="actief.length > 0">
            <h3 class="left">Playlist</h3>
            <ul class="list-group">
              <li class="list-group-item textleft act">
                <span class="badge badge-primary badge-pill right">{{ actief[0]['.value'] }}</span>
                <span class="left">{{ actief[2]['.value'] }}</span>
                <a class="right actionbuttons white" @click="verwijderen(actief[1]['.value'])"><i class="fa fa-minus fa-2x" aria-hidden="true"></i></a>
              </li>
            </ul>
          </div>
          <div class="form-group">
            <div class="row">
              <div class="col-sm-12">
                <button v-on:click="logout" name="register" class="form-control btn btn-login">Logout</button>
              </div>
            </div>
          </div>
        </div>
        <div v-show="error" class="alert alert-danger" role="alert">
          {{ error }}
        </div>
        <sweet-modal ref="modal" icon="error" hide-close-button blocking overlay-theme="dark" modal-theme="dark">
          <p>Weet je zeker dat je <strong v-show="deleterec.naam">{{ deleterec.naam }}</strong> wilt verwijderen?</p>
          <button type="button" class="btn btn-outline-danger verwijderen" v-on:click="permanent()" autofocus>Verwijderen</button>
          <button type="button" class="btn btn-outline-secondary annuleer" v-on:click="toggle()">Annuleren</button>
        </sweet-modal>
      </div>
    </div>
  </div>
</template>
<script>
/* eslint-disable */
import Vue from 'vue'
import firebase from 'firebase'
import { alldata } from '../assets/js/firebase'
import { actief } from '../assets/js/firebase'
import { db } from '../assets/js/firebase'
export default {
  name: 'Home',
  data () {
    return {
      records: [],
      actief: [],
      vorigrecord: null,
      error: null,
      access: false,
      modal: false,
      deleterec: {
        key: null,
        naam: null
      }
    }
  },
  firebase: {
    records: alldata,
    actief: actief    
  },
  created () {
  },
  methods: {
    verwijderen: function(record){
      let key = record;
      let naam = null;
      if (record.length > 1){
        naam = record;
      }else{
        naam = record['naam']
      }      
      this.error = null;
      alldata.child(key).update({ actief: false})   
      actief.remove()
    },
    toevoegen: function(record){
      let key = record['.key'];
      this.click = key;
      this.error = null;
      let naam = record['naam'];
      if(this.actief.length == 0){
        let datum = record['datum'];
        let waarden = record['waarden'];
        let rec = {
          'datum': datum,
          'naam': naam,
          'waarden': waarden,
          'key': key        
        }
        actief.set(rec);    
        alldata.child(key).update({ actief: true});
        this.vorigrecord = naam;
      }else{
        this.error = "Je kan maar 1 record tegelijk in de afspeellijst plaatsen. Verwijder eerst " + this.vorigrecord + "."
      }      
    },
    toggle: function(record){
      this.error = null;
      if(this.modal == false){
        this.deleterec.key = record['.key'];
        this.deleterec.naam = record['naam'];
        this.$refs.modal.open();
        this.modal = true
      }else{
        this.deleterec.key = null;
        this.deleterec.naam = null;
        this.$refs.modal.close()
        this.modal = false
      }
    },
    permanent: function(){
      alldata.child(this.deleterec.key).remove()
      this.$refs.modal.close()
      this.modal = false
      this.deleterec.key = null;
      this.deleterec.naam = null;
    },
    logout: function(){
      firebase.auth().signOut().then(()=>{
        this.$router.replace('login')
      })
    }
  }
}
</script>
