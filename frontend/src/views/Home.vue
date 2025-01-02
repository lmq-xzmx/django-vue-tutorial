<template>
  <div>
    <BlogHeader :user="user" @logout="handleLogout" />
    <div v-if="isAuthenticated">
      <ArticleList />
      <CategoryList />
      <TagList />
    </div>
    <div v-else>
      <p>请先登录以查看内容。</p>
      <router-link to="/login">登录</router-link>
    </div>
    <BlogFooter />
  </div>
</template>

<script>
import BlogHeader from '../components/BlogHeader.vue';
import ArticleList from '../components/ArticleList.vue';
import CategoryList from '../components/CategoryList.vue';
import TagList from '../components/TagList.vue';
import BlogFooter from '../components/BlogFooter.vue';
import { getCurrentUser, logout } from '../auth';

export default {
  name: 'Home',
  components: {
    BlogHeader,
    ArticleList,
    CategoryList,
    TagList,
    BlogFooter
  },
  data() {
    return {
      user: getCurrentUser()
    };
  },
  computed: {
    isAuthenticated() {
      return this.user && this.user.access;
    }
  },
  methods: {
    handleLogout() {
      logout();
      this.user = null;
      this.$router.push({ name: 'Login' });
    }
  }
};
</script>
