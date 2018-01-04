<template>
  <div class="main">
    <div class="container">
      <div class="card">
        <h1>Opgenomen</h1>
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
        <h1>Afspeellijst</h1>
         <ul class="list-group">
          <li class="list-group-item textleft act">
            <span class="badge badge-primary badge-pill right">{{ actief[0]['.value'] }}</span>
            <span class="left">{{ actief[2]['.value'] }}</span>
            <a class="right actionbuttons white" @click="verwijderen(actief[1]['.value'])"><i class="fa fa-minus fa-2x" aria-hidden="true"></i></a>
          </li>
        </ul>
      </div>
      <div v-show="error" class="alert alert-danger" role="alert">
        {{ error }}
      </div>
      <sweet-modal ref="modal" icon="error" hide-close-button blocking overlay-theme="dark" modal-theme="dark">
        <p>Weet je zeker dat je <strong v-show="deleterec.naam">{{ deleterec.naam }}</strong> wilt verwijderen?</p>
        <button type="button" class="btn btn-outline-danger verwijderen" v-on:click="permanent()">Verwijderen</button>
        <button type="button" class="btn btn-outline-secondary annuleer" v-on:click="toggle()">Annuleren</button>
      </sweet-modal>
    </div>
  </div>
</template>
<script>
/* eslint-disable */
import initializeApp from 'firebase'
const app = initializeApp.initializeApp({
  apiKey: 'AIzaSyCQlYBkHTw5Q6N6A7_ygs6w8OkrKPE44uY',
  authDomain: 'roboplot-1.firebaseapp.com',
  databaseURL: 'https://roboplot-1.firebaseio.com',
  projectId: 'roboplot-1',
  storageBucket: 'roboplot-1.appspot.com',
  messagingSenderId: '775004018292'
})
const db = app.database();
const ref = db.ref('actief')
const ref2 = db.ref('data')
export default {
  name: 'hello',
  data () {
    return {
      records: [],
      actief: null,
      vorigrecord: null,
      error: null,
      modal: false,
      deleterec: {
        key: null,
        naam: null
      }
    }
  },
  firebase: {
    records: ref2,
    actief: ref    
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
      ref2.child(key).update({ actief: false})   
      ref.remove()
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
        ref.set(rec);    
        ref2.child(key).update({ actief: true});
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
      ref2.child(this.deleterec.key).remove()
      this.$refs.modal.close()
      this.modal = false
      this.deleterec.key = null;
      this.deleterec.naam = null;
    }
  }
}
</script>
