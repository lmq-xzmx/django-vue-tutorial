<template>
  <div>
    <BlogHeader/>
    <div id="article-create">
      <h3>发表文章</h3>
      <form id="image_form">
        <div class="form-elem">
          <span>图片：</span>
          <input v-on:change="onFileChange" type="file" id="file" />
        </div>
      </form>
      <form>
        <div class="form-elem">
          <span>标题：</span>
          <input v-model="title" type="text" placeholder="输入标题" />
        </div>
        <div class="form-elem">
          <span>分类：</span>
          <span v-for="category in categories" :key="category.id">
            <button
              class="category-btn"
              :style="categoryStyle(category)"
              @click.prevent="chooseCategory(category)"
            >
              {{category.title}}
            </button>
          </span>
        </div>
        <div class="form-elem">
          <span>标签：</span>
          <input v-model="tags" type="text" placeholder="输入标签，用逗号分隔" />
        </div>
        <div class="form-elem">
          <span>正文：</span>
          <textarea v-model="body" placeholder="输入正文" rows="20" cols="80"></textarea>
        </div>
        <div class="form-elem">
          <button v-on:click.prevent="submit">提交</button>
        </div>
      </form>
    </div>
    <BlogFooter/>
  </div>
</template>

<script>
import BlogHeader from '@/components/BlogHeader.vue';
import BlogFooter from '@/components/BlogFooter.vue';
import axios from 'axios';

export default {
  name: 'ArticleCreate',
  components: { BlogHeader, BlogFooter },
  data() {
    return {
      title: '',
      body: '',
      categories: [],
      selectedCategory: null,
      tags: '',
      avatarID: null,
    };
  },
  mounted() {
    this.fetchCategories();
  },
  methods: {
    fetchCategories() {
      const token = localStorage.getItem('jwt_token'); // 修正此处的键名
      axios.get('/api/category/', {
        headers: { Authorization: 'Bearer ' + token }
      })
      .then(response => this.categories = response.data)
      .catch(error => {
        console.error('Error fetching categories:', error);
      });
    },
    onFileChange(event) {
      // 处理文件上传逻辑
    },
    chooseCategory(category) {
      this.selectedCategory = category;
    },
    submit() {
      // 提交文章逻辑
    }
  }
};
</script>

<style scoped>
.category-btn {
  margin-right: 10px;
}
#article-create {
  text-align: center;
  font-size: large;
}
form {
  text-align: left;
  padding-left: 100px;
  padding-right: 10px;
}
.form-elem {
  padding: 10px;
}
input {
  height: 25px;
  padding-left: 10px;
  width: 50%;
}
button {
  height: 35px;
  cursor: pointer;
  border: none;
  outline: none;
  background: steelblue;
  color: whitesmoke;
  border-radius: 5px;
  width: 60px;
}
</style>
