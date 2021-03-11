import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import colors from 'vuetify/lib/util/colors'

Vue.use(Vuetify);

const vuetify = new Vuetify({
    theme: { 
        themes:{
            light: {
                primary: colors.grey.darken2,
                secondary: colors.grey.darken1,
                info: colors.grey.lighten1,
                accent: '#1DB954',
                background: '#212121'
            }
        } 
    },
})

export default vuetify
