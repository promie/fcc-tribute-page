<template>
  <div>
    <h1 class="large-font">{{ title }}</h1>
    <ul>
      <li class="list-font" v-for="(event,index) in events" :key="index">
        <span class="year-style">{{ event.year }}</span>
        : {{ event.desc }}
      </li>
    </ul>
  </div>
</template>

<script>
import states from "../assets/data.json";

export default {
  name: "AboutMark",
  props: {
    title: String
  },
  data() {
    return {};
  },
  computed: {
    events() {
      return states.timeline.map(item => {
        return item;
      });
    }
  }
};
</script>

<style scoped>
h1,
h3 {
  position: relative;
  margin-left: 50px;
}

li {
  margin-left: 15px;
  list-style: none;
}

.large-font {
  font-size: 50px;
  color: #3b5998;
}

.list-font {
  font-size: 15px;
}

.year-style {
  color: #3b5998;
  font-size: 17px;
}
</style>


