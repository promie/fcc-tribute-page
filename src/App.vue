<template>
  <div id="app">
    <TributePage />
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
@import url("https://fonts.googleapis.com/css?family=Viga&display=swap");

body {
  font-family: "Viga", sans-serif;
  background:#fff;
  background-size: cover;
  margin-left: 50px;
  margin-right: 50px;
}
</style>
