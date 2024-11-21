<template>
  <div id="app">
    <!-- 根据 currentPage 动态加载组件 -->
    <component 
      :is="currentPage" 
      @switch="switchPage" 
      @authenticated="handleAuthentication" 
      :username="username" 
      :user_id="user_id" 
    />
  </div>
</template>

<script>
import LoginPage from './components/LoginPage.vue';
import RegisterPage from './components/RegisterPage.vue';
import MainPage from './components/MainPage.vue';

export default {
  name: 'App',
  data() {
    return {
      currentPage: 'LoginPage', // 当前页面
      username: '', // 用户名
      user_id: ''  // 用户 ID
    };
  },
  components: {
    LoginPage,
    RegisterPage,
    MainPage
  },
  methods: {
    // 页面切换方法
    switchPage(page) {
      this.currentPage = page === 'login' ? 'LoginPage' : 'RegisterPage';
    },
    // 处理登录成功的回调
    handleAuthentication({ page, username, user_id }) {
      this.currentPage = page; // 切换到 MainPage
      this.username = username; // 存储用户名
      this.user_id = user_id; // 存储用户 ID
    }
  }
};
</script>

<style>
body {
  font-family: Arial, sans-serif;
}
</style>
