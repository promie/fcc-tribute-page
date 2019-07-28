<template>
  <div id="app">
    <TributePage title="Evan You"/>
  </div>
</template>

<script>
import TributePage from './components/TributePage'

export default {
  name: 'app',
  components: {
    TributePage
  }
}
</script>

<style>
body {
  background-image: url('./assets/background.png');
  height: 100%;
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
}
</style>
