/* eslint-disable */
import firebase from '../../../node_modules/firebase'
const app = firebase.initializeApp({
    apiKey: 'AIzaSyCQlYBkHTw5Q6N6A7_ygs6w8OkrKPE44uY',
    authDomain: 'roboplot-1.firebaseapp.com',
    databaseURL: 'https://roboplot-1.firebaseio.com',
    projectId: 'roboplot-1',
    storageBucket: 'roboplot-1.appspot.com',
    messagingSenderId: '775004018292'
  })
  export const db = app.database()
  export const alldata = db.ref('data')
  export const actief = db.ref('actief')
