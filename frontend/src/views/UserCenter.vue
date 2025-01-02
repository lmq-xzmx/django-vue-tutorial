<template>
  <div>
    <BlogHeader />
    <h2>用户中心</h2>
    <UserAvatar />
    <BlogFooter />
  </div>
</template>

<script>
import BlogHeader from '../components/BlogHeader.vue';
import UserAvatar from '../components/UserAvatar.vue';
import BlogFooter from '../components/BlogFooter.vue';

export default {
  name: 'UserCenter',
  components: {
    BlogHeader,
    UserAvatar,
    BlogFooter
  }
};
</script>
