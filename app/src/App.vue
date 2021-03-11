<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          class="shrink mr-2"
          contain
          :src="require('../src/assets/logo.svg')"
          transition="scale-transition"
          width="40"
        />
      </div>
      <div class=" height: parent align-center">
        <h3 class= "display: block; font-weight bold; info--text; text-truncate ">
          Spotify Playlist Curator
        </h3>
      </div>
    </v-app-bar>

    <v-main>
      <HelloWorld/>
    </v-main>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld';

export default {
  name: 'App',

  components: {
    HelloWorld,
  },

  data: () => ({
    //
  }),
};
</script>
