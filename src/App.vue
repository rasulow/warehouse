<template>
  <v-app>

    <v-main>
      <side-bar
        v-if="$route.path != '/login'"
      />
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
// import is_have from './utils/haveToken';
import SideBar from "@/components/sidebar/SideBar.vue";
import is_have from "@/utils/haveToken";

export default {
  name: 'App',

  data: () => ({
  }),
  created() {
    this.checkUser()
  },
  mounted() {
    this.$axios.interceptors.response.use(
        (response) => {
          return response;
        },
        (error) => {
          if (error.response && error.response.status === 401) {
            window.location.reload();
          }
          return Promise.reject(error);
        }
    );
  },
  beforeDestroy() {
  }, 
  methods: {
    async checkUser() {
      if (!is_have()) {
          await this.$router.push('/login');
      }
    }
  },
  watch: {
  },
  components: {
    SideBar
  }
};
</script>

<style>
* {
    text-transform: unset !important;
    letter-spacing: normal;
}
</style>
