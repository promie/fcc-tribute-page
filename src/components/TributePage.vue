<template>
  <div class="app">
    <div class="header">
      <div class="header-one">
        <img :src="logo" alt="Vue Logo">
        <h2>{{ title }}</h2>
        <span>{{ description }}</span>
      </div>
    </div>

    <div class="content">
      <div class="content-one">
        <h3>Box Four</h3>
        <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Et quos adipisci nemo! Corrupti itaque nesciunt ea consequatur mollitia, sint dolorum quod exercitationem a ipsam fugit cupiditate commodi esse dolor autem.</p>
      </div>
      <div class="content-two">
        <h3>Box Five</h3>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Libero iusto voluptates quasi ad nulla, maxime excepturi at eaque qui doloribus voluptatibus similique. Obcaecati aspernatur voluptatibus consequuntur voluptatem laudantium. Cupiditate, mollitia.</p>
      </div>
    </div>

    <div class="footer">
      <div class="footer-one">
        <h3>Box Seven</h3>
        <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Et quos adipisci nemo! Corrupti itaque nesciunt ea consequatur mollitia, sint dolorum quod exercitationem a ipsam fugit cupiditate commodi esse dolor autem.</p>
      </div>
    </div>
  </div>
</template>

<script>
import logo from '../assets/logo.png'

export default {
  name: 'TributePage',
  props: {
    title: String
  },
  data() {
    return {
      logo,
      description: 'The genius behind VueJS'
    }
  }
}
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

.content {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}

.footer {
  display: flex;
  justify-content: center;
}

.content div, .footer div{
  border: 1px #ccc solid;
  padding: 10px;
}

.content-one {
  flex: 2;
}

.content-two {
  flex: 5;
}

</style>
