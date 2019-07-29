<template>
  <div id="app">
    <TributePage title="Evan You" />
  </div>
</template>

<script>
import TributePage from "./components/TributePage";

export default {
  name: "app",
  components: {
    TributePage
  }
};
</script>

<style>
body {
  background: #fff;
  background-size: cover;
}
</style>
