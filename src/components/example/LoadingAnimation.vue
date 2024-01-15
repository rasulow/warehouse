<script>
export default {
  data: () => ({
  }),
}
</script>

<template>
  <div class="loading-overlay">
    <v-progress-circular indeterminate color="#0BB923" size="50"/>
  </div>
</template>

<style scoped>
.loading-overlay {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 16px;
  border-radius: 8px;
}
</style>