<template>
  <div>
      <Description />
      <Predictor />
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