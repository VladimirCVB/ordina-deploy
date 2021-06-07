<template>
  <div id="app">
    <Header />
    <Content />
  </div>
</template>

<script>
import Header from './components/Header.vue'
import Content from './views/Content.vue'

export default {
  name: 'App',
  components: {
    Header,
    Content
  }
}
</script>