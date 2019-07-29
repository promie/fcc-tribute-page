<template>
  <div class="app">
    <div class="header">
      <div class="header-one">
        <img :src="logo" alt="Vue Logo" />
        <h2>{{ title }}</h2>
        <span>{{ description }}</span>
      </div>
    </div>

    <hr />

    <div class="content">
      <div class="content-one">
        <div class="polaroid">
          <img class="evan" :src="evan" alt="Picture of Evan You" />
          <div class="container">
            <p>Evan You at some bullshit event</p>
          </div>
        </div>
      </div>
      <div class="content-two">
        <h3>Box Five</h3>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Libero iusto voluptates quasi ad nulla, maxime excepturi at eaque qui doloribus voluptatibus similique. Obcaecati aspernatur voluptatibus consequuntur voluptatem laudantium. Cupiditate, mollitia.</p>
      </div>
    </div>

    <hr />

    <div class="footer">
      <div class="footer-one">
        <h3>Box Seven</h3>
        <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Et quos adipisci nemo! Corrupti itaque nesciunt ea consequatur mollitia, sint dolorum quod exercitationem a ipsam fugit cupiditate commodi esse dolor autem.</p>
      </div>
    </div>
  </div>
</template>

<script>
import logo from "../assets/logo.png";
import evan from "../assets/evan-you.jpg";

export default {
  name: "TributePage",
  props: {
    title: String
  },
  data() {
    return {
      logo,
      evan,
      description: "The genius behind VueJS"
    };
  }
};
</script>

<style scoped>
.app {
  margin-top: 15px;
  text-align: center;
}

.header {
  display: flex;
  justify-content: center;
}

@media only screen and (min-width: 640px) {
  .content {
    display: flex;
    justify-content: space-between;
    margin-top: 30px;
  }
}

.footer {
  display: flex;
  justify-content: center;
}

.content-one {
  flex: 3;
}

.content-two {
  flex: 5;
}

.polaroid {
  width: 80%;
  background-color: white;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  margin-bottom: 25px;
  margin: 25px;
  border-radius: 8px;
  align-content: center;
}

.container {
  text-align: center;
  padding: 10px 20px;
}

.evan {
  width: 100%;
}
</style>
