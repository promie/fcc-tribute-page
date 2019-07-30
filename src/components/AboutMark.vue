<template>
  <div>
    <h1>Hello.</h1>
    <h3>My name is {{ title }}</h3>
    <ul>
      <li v-for="(event,index) in events" :key="index">{{ event.year }}: {{ event.desc }}</li>
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

</style>


