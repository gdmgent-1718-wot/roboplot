<template>
  <div class="main">
    <div class="container">
      <div class="card">
        <h1>Opgenomen</h1>
        <ul class="list-group">
          <li class="list-group-item textleft" v-for="records in records" v-bind:class="{ act: records.actief }">
            <span class="badge badge-primary badge-pill">{{ records.datum }}</span>
            <span class="left">{{ records.naam }}</span>
            <a class="right actionbuttons" @click="toevoegen(records.naam)" v-show="!records.actief"><i class="fa fa-plus fa-2x" aria-hidden="true"></i></a>
            <a class="right actionbuttons" @click="verwijderen(records.naam)" v-show="records.actief"><i class="fa fa-minus fa-2x" aria-hidden="true"></i></a>
          </li>
        </ul>
        <nav aria-label="Page navigation example" v-if="records.length >= 5">
          <ul class="pagination justify-content-end">
            <li class="page-item disabled">
              <a class="page-link" href="#" tabindex="-1">Vorige</a>
            </li>
            <li class="page-item"><a class="page-link" href="#">1</a></li>
            <li class="page-item"><a class="page-link" href="#">2</a></li>
            <li class="page-item"><a class="page-link" href="#">3</a></li>
            <li class="page-item">
              <a class="page-link" href="#">Volgende</a>
            </li>
          </ul>
        </nav>
      </div>
      <div class="card" v-show="actief">
        <h1>Afspeellijst</h1>
         <ul class="list-group">
          <li class="list-group-item textleft act" v-for="actief in actief">
            <span class="badge badge-primary badge-pill right">{{ actief.datum }}</span>
            <span class="left">{{ actief.naam }}</span>
            <a class="right actionbuttons white" @click="verwijderen(actief.naam)"><i class="fa fa-minus fa-2x" aria-hidden="true"></i></a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>
<script>
/* eslint-disable */
import * as firebase from "firebase";
export default {
  name: 'hello',
  data () {
    return {
      records: [],
      actief: null
    }
  },
  created () {
    this.getlogs();
  },
  methods: {
    getlogs: function () {  
      let self = this;
      firebase.database().ref('data').on('value', function (logs) {
        self.records = logs.val()
      });
      firebase.database().ref('actief').on('value', function (actief) {
        self.actief = actief.val()
      })
    },
    verwijderen: function(naam){
      
    },
    toevoegen: function(naam){
      if(this.actief = null){
      }
    }
  }
}
</script>
