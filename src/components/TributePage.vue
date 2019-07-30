<template>
  <div class="app">
    <div class="content">
      <div class="content-one">
        <AboutMark title="Mark Zuckerberg" />
      </div>
      <div class="content-two">
        <img class="responsive" :src="zuckerberg" alt="A Picture of Mark Zuckerberg" />
      </div>
    </div>
  </div>
</template>

<script>
import AboutMark from "./AboutMark";
import zuckerberg from "../assets/zuckerberg.png";

export default {
  name: "TributePage",
  components: {
    AboutMark
  },
  props: {},
  data() {
    return {
      zuckerberg
    };
  }
};
</script>

<style scoped>
@media only screen and (min-width: 640px) and (min-width: 400px) {
  .content {
    display: flex;
    justify-content: space-between;
    margin-top: 10vh;
  }
}

/* .content div {
  border-style: solid;
} */

.content-one {
  flex: 1;
}

.content-two {
  flex: 1;
}

.responsive {
  width: 60%;
  height: auto;
  margin-left: 20%;
}
</style>
