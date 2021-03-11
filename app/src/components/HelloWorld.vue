<template>
  <v-app id="main" :style="{background: $vuetify.theme.themes[theme].background}">
    <v-container>
      <v-row class="text-center">
        <v-col cols="12">
          <v-img
            :src="require('../assets/logo.svg')"
            class="my-3"
            contain
            height="200"
          />
        </v-col>

        <v-col class="mb-4">
          <h1 class="display-2 font-weight-bold mb-3 info--text">
            Welcome to Spotify Playlist Curator
          </h1>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
  export default {
    name: 'HelloWorld',

    data: () => ({
      ecosystem: [
        {
          text: 'vuetify-loader',
          href: 'https://github.com/vuetifyjs/vuetify-loader',
        },
        {
          text: 'github',
          href: 'https://github.com/vuetifyjs/vuetify',
        },
        {
          text: 'awesome-vuetify',
          href: 'https://github.com/vuetifyjs/awesome-vuetify',
        },
      ],
      importantLinks: [
        {
          text: 'Documentation',
          href: 'https://vuetifyjs.com',
        },
        {
          text: 'Chat',
          href: 'https://community.vuetifyjs.com',
        },
        {
          text: 'Made with Vuetify',
          href: 'https://madewithvuejs.com/vuetify',
        },
        {
          text: 'Twitter',
          href: 'https://twitter.com/vuetifyjs',
        },
        {
          text: 'Articles',
          href: 'https://medium.com/vuetify',
        },
      ],
      whatsNext: [
        {
          text: 'Explore components',
          href: 'https://vuetifyjs.com/components/api-explorer',
        },
        {
          text: 'Select a layout',
          href: 'https://vuetifyjs.com/getting-started/pre-made-layouts',
        },
        {
          text: 'Frequently Asked Questions',
          href: 'https://vuetifyjs.com/getting-started/frequently-asked-questions',
        },
      ],
    }),
    computed:{
      theme(){
        return (this.$vuetify.theme.dark) ? 'dark' : 'light'
      }
    }
  }
</script>
<style lang="scss">
  .h1{
    // color: '$vuetify.theme.themes[theme].info';
    color: '#e0e0e0'
  }
</style>
