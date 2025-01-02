<template>
  <header>
    <h1>我的博客</h1>
    <nav>
      <router-link to="/">首页</router-link>
      <router-link to="/user-center">用户中心</router-link>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'BlogHeader'
};
</script>

<style scoped>
header {
  background-color: #f8f9fa;
  padding: 10px;
}
nav a {
  margin-right: 10px;
}
</style>
