<template>
  <div class="border-2 border-yellow-600 rounded-lg">
      <!-- Predictor Title -->
      <div class="text-white text-center text-2xl bg-yellow-600 shadow-lg">
        <i class="fas fa-history mr-2 text-lg"></i>
        <label>Predictor</label>
      </div>

      <!-- Content 'From' and 'To'   -->
      <div class="p-5 divide-y divide-yellow-600 text-2xl">
        <select name="cars" id="cars" class="block w-full outline-none cursor-pointer">
          <option value="" disabled selected>From</option>
          <option v-for="station in stations" :key="station" value='station'>{{station}}</option>
        </select>

        <!-- <hr class="mt-2 mb-2 white text-white"/> -->

        <select name="cars" id="cars" class="block w-full outline-none cursor-pointer">
          <option value="" disabled selected>To</option>
          <option v-for="station in stations" :key="station" value='station'>{{station}}</option>
        </select>
      </div>

      <!-- Departure Date Title -->
      <div class="bg-yellow-600 text-white text-center text-2xl shadow-lg">
        <i class="fas fa-train mr-2 text-lg"></i>
        <label>Departure Date</label>
      </div>
      
      <!-- Date Content -->
      <div class="mt-5 mb-64 p-2 divide-y divide-yellow-500">
        <input type="date" placeholder="Date" class="w-full outline-none text-xl" />
        <hr />

      </div>

      <!-- Predict Button -->
      <div class="text-center mb-5">
        <button class="bg-yellow-600 rounded-md text-white p-2 text-2xl w-5/6 shadow-lg hover:bg-gray-700 hover:text-yellow-600 hover:shadow-none ease-in duration-200 focus:outline-none">Make Prediction</button>
      </div>
  </div>  
</template>

<script>
export default {
  name: 'Predictor',
  props: {
  },
  data() {
    return {
      stations: ['Groningen', 'Den Haag', 'Amsterdam', 'Utrecht', 'Eindhoven'],
    }
  }, 
}
</script>