<template>
  <div class="border-2 border-yellow-600 rounded-lg">
      <!-- Predictor Title -->
      <div class="text-white text-center text-2xl bg-yellow-600 shadow-lg">
        <i class="fas fa-history mr-2 text-lg"></i>
        <label>Predictor</label>
      </div>

      <!-- Content 'From' and 'To'   -->
      <div class="p-5 divide-y divide-yellow-600 text-2xl">
        <select v-model="form.fromStation" name="fromStation" class="block w-full outline-none cursor-pointer">
          <option value="" disabled selected>From</option>
          <option v-for="(station, index) in stationCodes" :key="station" v-bind:value="station">{{stations[index]}}</option>
        </select>

        <!-- <hr class="mt-2 mb-2 white text-white"/> -->

        <select v-model="form.toStation" name="toStation" class="block w-full outline-none cursor-pointer">
          <option value="" disabled selected>To</option>
          <option v-for="(station, index) in stationCodes" :key="station" v-bind:value="station">{{stations[index]}}</option>
        </select>
      </div>

      <!-- Departure Date Title -->
      <div class="bg-yellow-600 text-white text-center text-2xl shadow-lg">
        <i class="fas fa-train mr-2 text-lg"></i>
        <label>Departure Date</label>
      </div>
      
      <!-- Date Content -->
      <div class="mt-5 mb-10 p-2 divide-y divide-yellow-500">
        <input v-model="inputTime" type="date" placeholder="Date" class="w-full outline-none text-xl" />
        <hr />
      </div>

      <!-- Results Title -->
      <div class="bg-yellow-600 text-white text-center text-2xl shadow-lg">
        <i class="fas fa-business-time mr-2 text-lg"></i>
        <label>Results</label>
      </div>

      <!-- Results Content -->
      <div class="mt-5 mb-10 p-2 text-xl">
        <label v-if="result">{{result}}</label>
      </div>

      <!-- Errors -->
      <div class="text-red-700" v-if="errors.length">
        <div class="bg-red-600 text-white text-center text-2xl shadow-lg">
          <i class="fas fa-exclamation-circle mr-2"></i>
          <label>Errors Occurred</label>
        </div>
        <div class="p-5 font-bold">
          <p v-for="error in errors" :key="error">{{error}}</p>
        </div>  
      </div>

      <!-- Predict Button -->
      <div class="text-center mb-5">
        <button v-on:click="checkForm" class="bg-yellow-600 rounded-md text-white p-2 text-2xl w-5/6 shadow-lg hover:bg-gray-700 hover:text-yellow-600 hover:shadow-none ease-in duration-200 focus:outline-none">Make A Prediction</button>
      </div>
  </div>  
</template>

<script>
import axios from "axios"
import moment from 'moment'

export default {
  name: 'Predictor',
  props: {
  },
  data() {
    return {
      stations: ['Groningen', 'Den Haag', 'Amsterdam', 'Utrecht', 'Eindhoven', 'Rotterdam'],
      stationCodes: ['GN', 'GVC', 'ASD', 'UT', 'EHV', 'RTD'],
      inputTime: '',
      form : {
        fromStation: '',
        toStation: '',
        time: ''
      },
      result: '',
      errors: []
    }
  },
  methods:{
    checkForm: function (e) {

      this.errors = [];

      if (!this.form.fromStation) {
        this.errors.push('Departure station required!');
        return;
      }
      if (!this.form.toStation) {
        this.errors.push('Arrival station required!');
        return;
      }

      if (!this.inputTime) {
        this.errors.push('Date required!');
        return;
      }

      if (this.form.fromStation == this.form.toStation) {
        this.errors.push('Departure and Arrival stations cannot be the same!');
        return;
      }

      this.form.time = moment(String(this.inputTime)).format('2015-MM-DD');

      axios
      .post('http://127.0.0.1:5000/', this.form)
      .then(response =>{

        if(response.data == 0){
          this.result = "The model predicted that there will be no delay on this route.";
        }          

        else if(response.data == 1){
          this.result = "The model predicted that there will a delay of less than 5 minutes on this route.";
        }          

        else if(response.data == 2){
          this.result = "The model predicted that there will a delay of more than 5 minutes on this route.";
        }        

        else{
          this.result = "We are sorry! " + response.data;
        }
          
      })

      e.preventDefault();
    }
  } 
}
</script>