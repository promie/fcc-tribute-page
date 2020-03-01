<script>
import TributePage from '@/views/TributePage.vue'

export default {
  name: 'App',
  components: {
    TributePage
  }
}
</script>

<template>
  <div>
    <TributePage />
  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css?family=Viga&display=swap');

body {
  font-family: 'Viga', sans-serif;
  background: #3b5998;
  background-size: cover;
  margin-left: 50px;
  margin-right: 50px;
  box-shadow: 3px 3px 5px 6px #ccc;
}
</style>
