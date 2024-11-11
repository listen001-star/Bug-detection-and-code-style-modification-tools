<template>
  <div class="vh-100 d-flex flex-column">
    <!-- 顶部横向栏，包含用户问候、页面选择和登出按钮 -->
    <div class="top-bar d-flex justify-content-between align-items-center p-3">
      <div class="d-flex align-items-center">
        <span class="username-display mr-5">Hello, {{ username }}</span>
        <button class="btn btn-page mr-3" :class="{ active: currentView === 'main' }" @click="currentView = 'main'">Main</button>
        <button class="btn btn-page mr-3" :class="{ active: currentView === 'history' }" @click="currentView = 'history'">History</button>
        <button @click="logout" class="btn btn-page">Logout</button>
      </div>
    </div>

    <!-- 主内容区域 -->
    <div class="flex-grow-1 p-4">
      <div v-if="currentView === 'main'">
        <div class="card p-5 shadow rounded">
          <h2 class="mb-4">Welcome to Main Page</h2>
          <div class="mb-4">
            <h3>Upload Python File</h3>
            <input type="file" class="form-control-file" accept=".py" />
          </div>
          <div class="mb-4">
            <h3>Execute Command</h3>
            <button class="btn btn-analyze btn-block" @click="showResults = true">Analyze with Pylint</button>
          </div>
          <div v-if="showResults" class="mt-4">
            <h3>Results</h3>
            <p>Score: 85</p>
            <div class="static-pie-chart">
              <p>Syntax Errors: 40%</p>
              <p>Logic Errors: 35%</p>
              <p>Style Issues: 25%</p>
            </div>
          </div>
        </div>
      </div>

      <div v-if="currentView === 'history'">
        <div class="card p-5 shadow rounded">
          <h2 class="mb-4">History Data</h2>
          <ul>
            <li class="mb-3">
              <span>2024-11-10 10:00 - analysis1.py</span>
              <button class="btn btn-view-result ml-3" @click="showModal = true">查看结果</button>
            </li>
            <li class="mb-3">
              <span>2024-11-10 11:00 - analysis2.py</span>
              <button class="btn btn-view-result ml-3" @click="showModal = true">查看结果</button>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <!-- 弹窗显示静态结果 -->
    <div v-if="showModal" class="modal-overlay">
      <div class="modal-content">
        <h3>Analysis Result</h3>
        <p>Score: 85</p>
        <div class="static-pie-chart">
          <p>Syntax Errors: 40%</p>
          <p>Logic Errors: 35%</p>
          <p>Style Issues: 25%</p>
        </div>
        <button class="btn btn-close-modal mt-3" @click="showModal = false">Close</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MainPage',
  data() {
    return {
      username: 'User',
      currentView: 'main', // 初始界面设置为 'main'
      showResults: false,
      showModal: false,
    };
  },
  methods: {
    logout() {
      this.$emit('switch', 'LoginPage'); // 触发事件通知父组件切换到登录界面
    },
  },
};
</script>

<style scoped>
.top-bar {
  background-color: #f8f9fa;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  padding: 0.75rem 1.5rem;
}

.username-display {
  font-weight: 600;
  color: #333;
  font-size: 1.25rem;
}

.btn-page {
  background: transparent;
  border: none;
  color: #333;
  font-size: 1rem;
  font-weight: 600;
  transition: all 0.3s ease;
  padding: 0.5rem 1rem;
  border-radius: 8px;
}

.btn-page.active {
  background-color: #e9ecef;
}

.btn-page:hover {
  background-color: #ddd;
}

.card {
  border-radius: 15px;
  padding: 2.5rem;
  background: rgba(255, 255, 255, 0.9);
  box-shadow: 0 6px 30px rgba(0, 0, 0, 0.15);
}

h2, h3 {
  color: #333;
}

.form-control-file {
  border-radius: 8px;
  border: 1px solid #ccc;
}

.result-box {
  white-space: pre-wrap;
  background-color: #f8f9fa;
  padding: 15px;
  border-radius: 8px;
}

.static-pie-chart {
  background-color: #f1f1f1;
  padding: 10px;
  border-radius: 8px;
  text-align: left;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content {
  background: #fff;
  padding: 2rem;
  border-radius: 8px;
  width: 300px;
  text-align: center;
}

.btn-close-modal {
  padding: 0.5rem 1rem;
  background-color: #d9534f;
  color: #fff;
  border: none;
  border-radius: 4px;
}

.btn-analyze {
  background: linear-gradient(to right, #43cea2, #185a9d);
  color: #fff;
  border: none;
}

.btn-view-result {
  background: #5bc0de;
  color: #fff;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 8px;
}

.btn-analyze:hover, .btn-view-result:hover {
  background-color: #499ecf;
}
</style>
