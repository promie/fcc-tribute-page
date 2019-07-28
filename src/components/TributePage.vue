<template>
  <div>
    <div class="container-1">
      <div class="box-1">
        <h3>Box One</h3>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
      </div>
      <div class="box-2">
        <h3>Box Two</h3>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
      </div>
      <div class="box-3">
        <h3>Box Three</h3>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
      </div>
    </div>

    <div class="container-2">
      <div class="container-2-box">
        <h3>Box Four</h3>
        <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Et quos adipisci nemo! Corrupti itaque nesciunt ea consequatur mollitia, sint dolorum quod exercitationem a ipsam fugit cupiditate commodi esse dolor autem.</p>
      </div>
      <div class="container-2-box">
        <h3>Box Five</h3>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Libero iusto voluptates quasi ad nulla, maxime excepturi at eaque qui doloribus voluptatibus similique. Obcaecati aspernatur voluptatibus consequuntur voluptatem laudantium. Cupiditate, mollitia.</p>
      </div>
      <div class="container-2-box">
        <h3>Box Six</h3>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis porro placeat laborum voluptas, repellat, ipsa rerum voluptate repudiandae inventore, repellendus corporis atque voluptatem sunt maiores earum sapiente veniam ducimus assumenda!</p>
      </div>
    </div>

    <div class="container-3">
      <div class="container-3-box">
        <h3>Box Seven</h3>
        <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Et quos adipisci nemo! Corrupti itaque nesciunt ea consequatur mollitia, sint dolorum quod exercitationem a ipsam fugit cupiditate commodi esse dolor autem.</p>
      </div>
      <div class="container-3-box">
        <h3>Box Eight</h3>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Libero iusto voluptates quasi ad nulla, maxime excepturi at eaque qui doloribus voluptatibus similique. Obcaecati aspernatur voluptatibus consequuntur voluptatem laudantium. Cupiditate, mollitia.</p>
      </div>
      <div class="container-3-box">
        <h3>Box Nine</h3>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis porro placeat laborum voluptas, repellat, ipsa rerum voluptate repudiandae inventore, repellendus corporis atque voluptatem sunt maiores earum sapiente veniam ducimus assumenda!</p>
      </div>
      <div class="container-3-box">
        <h3>Box Ten</h3>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis porro placeat laborum voluptas, repellat, ipsa rerum voluptate repudiandae inventore, repellendus corporis atque voluptatem sunt maiores earum sapiente veniam ducimus assumenda!</p>
      </div>
      <div class="container-3-box">
        <h3>Box Eleven</h3>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis porro placeat laborum voluptas, repellat, ipsa rerum voluptate repudiandae inventore, repellendus corporis atque voluptatem sunt maiores earum sapiente veniam ducimus assumenda!</p>
      </div>
      <div class="container-3-box">
        <h3>Box Twelve</h3>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis porro placeat laborum voluptas, repellat, ipsa rerum voluptate repudiandae inventore, repellendus corporis atque voluptatem sunt maiores earum sapiente veniam ducimus assumenda!</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TributePage',
  props: {
    title: String
  },
  data() {
    return {

    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

@media(min-width:468px) {
    .container-1 {
      display: flex;
      /* align-items: flex-start;
      align-items: flex-end;
      align-items: center;

      flex-direction: column; */
  }

  .container-2 {
      display: flex;
      /* justify-content: flex-start;
      justify-content: flex-end;
      justify-content: center; 
      justify-content: space-around */
      justify-content: space-between;
  }
}

.container-3{
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}


.container-1 div, .container-2 div, .container-3 div{
  border: 1px #ccc solid;
  padding: 10px;
}

.box-1 {
  flex: 2;
  order: 2;
}

.box-2 {
  flex: 1;
  order: 1;
}

.box-3 {
  flex: 1;
  order: 3;
}

.container-2-box {
  flex-basis: 27%;
}

.container-3-box {
  flex-basis: 12%
}

</style>
