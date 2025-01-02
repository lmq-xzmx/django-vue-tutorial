import {
    createRouter,
    createWebHistory
} from 'vue-router';
import Home from '../views/Home.vue';
import ArticlePage from '../views/ArticlePage.vue';
import UserCenter from '../views/UserCenter.vue';
import ArticleEdit from '@/views/ArticleEdit.vue';
import Login from '../components/Login.vue';

const routes = [{
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/article/:id',
        name: 'ArticlePage',
        component: ArticlePage
    },
    {
        path: '/article/edit/:id',
        name: 'ArticleEdit',
        component: ArticleEdit
    },
    {
        path: '/user-center',
        name: 'UserCenter',
        component: UserCenter
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
        }

];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
});

export default router;