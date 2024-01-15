import '@fortawesome/fontawesome-free/css//all.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);

export default new Vuetify({
    icons: {
        iconfont: 'fa' || 'md'
    },
    theme: {
        themes: {
            dark: {
                background: '#616161'
            },
            light: {
                background: '#ff141d'
            }
        }
    },
    color: {
        main: '#7FBA5E',
        secondary: '#0BB923'
    }
});
