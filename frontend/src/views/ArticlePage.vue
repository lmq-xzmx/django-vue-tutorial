<template>
  <div>
    <BlogHeader />
    <ArticleDetail />
    <BlogFooter />
  </div>
</template>

<script>
import BlogHeader from '../components/BlogHeader.vue';
import ArticleDetail from '../components/ArticleDetail.vue';
import BlogFooter from '../components/BlogFooter.vue';

export default {
  name: 'ArticlePage',
  components: {
    BlogHeader,
    ArticleDetail,
    BlogFooter
  }
};
</script>
