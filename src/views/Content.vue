<template>
  <div>
    <div class="max-w-screen-xl mx-auto pt-10">
      <div class="-mx-4 flex flex-wrap">
        <Description class="w-full flex flex-col p-4 sm:w-1/2 lg:w-2/4 mr-5" />
        <Predictor class="inline-block w-1/3 flex flex-col justify-between" />
      </div>
    </div>
  </div>  
</template>

<script>
import Description from '../components/content/Description.vue'
import Predictor from '../components/content/Predictor.vue'

export default {
  name: 'Content',
  props: {
      
  },
  components: {
    Description,
    Predictor
  }
}
</script>