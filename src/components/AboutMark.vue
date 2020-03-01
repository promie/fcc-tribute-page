<script>
import TimelineInformation from '@/components/__mocks__/results.data'

export default {
  name: 'AboutMark',
  props: {
    title: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      events: TimelineInformation
    }
  }
}
</script>

<template>
  <div class="about-mark">
    <h1 class="large-font">{{ title }}</h1>
    <ul>
      <li class="list-font" v-for="(event, index) in events" v-bind:key="index">
        <span class="year-style">{{ event.year }}</span>
        : {{ event.desc }}
      </li>
    </ul>
    <hr />
    <div class="author">
      Developed By <span class="promie">Promie Yutasane</span>
    </div>
  </div>
</template>

<style scoped>
/* Mobile First Approach */
.about-mark {
  padding: 5px;
}

.large-font {
  font-size: 30px;
  text-align: center;
  color: #3b5998;
}

ul {
  padding: 3px;
}

li {
  list-style: none;
}

.list-font {
  font-size: 12px;
  line-height: 20px;
  text-align: justify;
}

.year-style {
  color: #3b5998;
  font-size: 15px;
}

.author {
  font-size: 12px;
  text-align: center;
  margin: 5px 0px;
}

.promie {
  color: #3b5998;
}

@media only screen and (min-width: 768px) {
  /* For desktop: */
  .large-font {
    font-size: 50px;
  }

  ul {
    padding-right: 50px;
  }

  .list-font {
    font-size: 15px;
  }
  .year-style {
    font-size: 17px;
  }

  .author {
    font-size: 15px;
    text-align: end;
    padding-right: 50px;
  }
}
</style>
