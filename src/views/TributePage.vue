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
    <figure id="img-div" class="tribute-img">
      <img
        id="image"
        class="zuckerberg"
        v-bind:src="zuckerberg"
        alt="A Picture of Mark Zuckerberg"
      />
      <figcaption id="img-caption" class="caption">
        An illustration of Mark Zuckerberg
      </figcaption>
    </figure>

    <div class="tribute-details" id="tribute-info">
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
  max-width: 200px;
  display: block;
  height: auto;
  padding: 10px 0;
  margin: 0 auto;
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
    max-width: 55%;
    display: block;
    height: auto;
    padding: 10px 0;
    margin: 0 auto;
  }

  .caption {
    margin-bottom: 10px;
  }
}
</style>
