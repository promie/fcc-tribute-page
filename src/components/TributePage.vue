<template>
  <div class="hello">
    <h1>Tribute To {{ title }}</h1>
    <p>The mastermind behind VueJS</p>
  </div>
</template>

<script>
export default {
  name: 'TributePage',
  props: {
    title: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
