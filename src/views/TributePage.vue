<script>
import AboutMark from '@/components/AboutMark.vue'
import ZuckerbergImage from '@/assets/zuckerberg.png'

export default {
  name: 'TributePage',
  components: {
    AboutMark
  },
  data() {
    return {
      title: 'Mark Zuckerberg',
      zuckerberg: ZuckerbergImage
    }
  }
}
</script>

<template>
  <div class="tribute">
    <div class="tribute-img">
      <img
        class="zuckerberg"
        v-bind:src="zuckerberg"
        alt="A Picture of Mark Zuckerberg"
      />
    </div>

    <div class="tribute-details">
      <about-mark v-bind:title="title" />
    </div>
  </div>
</template>

<style scoped>
/* Mobile First Approach */
.tribute {
  margin-top: 50px;
  background: #fff;
  display: flex;
  flex-direction: column;
}

.tribute-img {
  flex: 1;
  text-align: center;
}

.tribute-details {
  flex: 1;
}

.zuckerberg {
  width: 200px;
}

@media only screen and (min-width: 768px) {
  /* For desktop: */
  .tribute {
    display: flex;
    flex-direction: row;
  }

  .tribute-img {
    flex: 1;
  }

  .tribute-details {
    flex: 1;
  }

  .zuckerberg {
    width: 500px;
    padding: 10px 0;
  }
}
</style>
