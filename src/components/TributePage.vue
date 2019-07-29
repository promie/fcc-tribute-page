<template>
  <div class="app">

    <div class="content">
      <div class="content-one">
        <h3>Box One</h3>
        <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Exercitationem delectus et aliquam, distinctio, nulla optio id placeat nemo esse beatae atque sint dignissimos cupiditate, corporis sapiente maiores velit amet nihil!</p>
      </div>
      <div class="content-two">
        <img :src="zuckerberg" alt="A Picture of Mark Zuckerberg">
      </div>
    </div>

  </div>
</template>

<script>
import zuckerberg from '../assets/zuckerberg.png'

export default {
  name: "TributePage",
  props: {
    title: String
  },
  data() {
    return {
      zuckerberg
    };
  }
};
</script>

<style scoped>

@media only screen and (min-width: 640px) {
  .content {
    display: flex;
    justify-content: space-between;
    margin-top: 10vh;
  }
}

.content div {
  border-style: solid
}

.content-one {
  flex: 5;
}

.content-two {
  flex: 5;
}


</style>
