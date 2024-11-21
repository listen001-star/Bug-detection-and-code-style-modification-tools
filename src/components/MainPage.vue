<template>
  <div class="vh-100 d-flex flex-column">
    <!-- 顶部横向栏 -->
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
            <input type="file" class="form-control-file" accept=".py" @change="handleFileUpload" />
          </div>
          <div class="mb-4">
            <h3>Execute Command</h3>
            <button class="btn btn-analyze btn-block" @click="analyze">Analyze with Pylint</button>
          </div>
          <div v-if="showResults" class="mt-4">
            <h3>Results</h3>
            <p>Score: {{ analysisData?.data?.error?.Score || 'N/A' }}</p>
            
            <!-- 显示分析结果 -->
            <div class="results-container">
              <h4>Details</h4>
              <div class="scroll-box">
                <ul>
                  <li v-for="(result, index) in analysisData.data.results" :key="index">
                    Line: {{ result.Line }}, Error Type: {{ result["Error Type"] }}, 
                    Message: {{ result.Message }}, RuleID: {{ result.RuleID }}
                  </li>
                </ul>
              </div>
            </div>

            <!-- 聊天框 -->
            <div class="chat-container mt-4">
              <h4>Chat</h4>
              <div class="chat-box">
                <div v-for="(msg, index) in chatMessages" :key="index" class="chat-message">
                  <span class="user">{{ msg.user }}:</span>
                  <span class="message">{{ msg.text }}</span>
                </div>
              </div>
              <div class="chat-input">
                <input 
                  type="text" 
                  v-model="newMessage" 
                  placeholder="Ask a question..." 
                  @keyup.enter="sendMessage"
                />
                <button class="btn btn-primary" @click="sendMessage">Send</button>
              </div>
            </div>
            
            <div class="charts-container d-flex">
              <BarChart :data="barData" />
              <PieChart :data="pieData" />
            </div>
          </div>
        </div>
      </div>

      <div v-if="currentView === 'history'">
        <HistoryPage />
      </div>
    </div>
  </div>
</template>

<script>
import BarChart from './BarChart.vue';
import PieChart from './PieChart.vue';
import HistoryPage from './HistoryPage.vue';

export default {
  name: 'MainPage',
  components: {
    BarChart,
    PieChart,
    HistoryPage,
  },
  data() {
    return {
      chatMessages: [
        { user: 'GPT', text: 'Hi! Ask me anything about your results or coding.' }, // 默认欢迎消息
      ],
      newMessage: '',
      user_id: '4',
      username: 'User',
      currentView: 'main', // 初始界面设置为 'main'
      showResults: false,
      analysisData: null,
      defaultAnalysisData: {
        success: true,
        data: {
          results: [
            { Line: "8", "Error Type": "C0301", Message: "Line too long", RuleID: "line-too-long" },
            { Line: "38", "Error Type": "C0305", Message: "Trailing newlines", RuleID: "trailing-newlines" },
            { Line: "1", "Error Type": "C0114", Message: "Missing module docstring", RuleID: "missing-module-docstring" },
          ],
          error: {
            C: 14,
            W: 10,
            E: 11,
            R: 5,
            Score: 9,
          },
        },
      },
      selectedFile: null,
    };
  },
  computed: {
    pieData() {
      // if (!this.analysisData) return [];
       const { C, W, E, R } = this.analysisData.data.error;
      // return [C, W, E, R];
      const total = C + W + E + R; // 计算总数
    if (total === 0) return []; // 防止除以0
    return [
      (C / total * 100).toFixed(2),
      (W / total * 100).toFixed(2),
      (E / total * 100).toFixed(2),
      (R / total * 100).toFixed(2),
    ];
    },
    barData() {
      if (!this.analysisData) return [];
      const { C, W, E, R } = this.analysisData.data.error;
      return [C, W, E, R];
    },
  },
  methods: {
    async sendMessage() {
      if (this.newMessage.trim()) {
      const question = this.newMessage;
      this.chatMessages.push({ user: 'User', text: question }); // 添加用户消息

      try {
        const response = await fetch("http://127.0.0.1:8000/gpt/", {
         method: "POST",
         headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ question }),
        });

      if (response.ok) {
        const data = await response.json();
        if (data.success) {
          this.chatMessages.push({ user: 'GPT', text: data.data }); // 添加 GPT 回复
        } else {
          this.chatMessages.push({ user: 'GPT', text: "Sorry, I couldn't answer that." });
        }
      } else {
        this.chatMessages.push({ user: 'GPT', text: "Error connecting to the server." });
      }
      } catch (error) {
      this.chatMessages.push({ user: 'GPT', text: "Error connecting to the server." });
      }

    this.newMessage = ''; // 清空输入框
  }
},

    async analyze() {
      if (!this.selectedFile) {
        alert("Please upload a file first!");
        return;
      }

      const formData = new FormData();
      formData.append("upload_file", this.selectedFile);

      try {
        const response = await fetch("http://127.0.0.1:8000/file/analyse/", {
          method: "POST",
          headers: {
            Accept: "application/json",
          },
          body: formData,
        });

        if (response.ok) {
          const data = await response.json();
          this.analysisData = data;
        } else {
          console.error("Failed to fetch data from server. Using default data.");
          this.analysisData = this.defaultAnalysisData;
        }
      } catch (error) {
        console.error("Error while fetching data:", error);
        this.analysisData = this.defaultAnalysisData;
      }

      this.showResults = true;
    },
    handleFileUpload(event) {
      this.selectedFile = event.target.files[0];
    },
    logout() {
      this.$emit("switch", "LoginPage"); // 切换到登录页面
    },
  },
};
</script>

<style scoped>
.charts-container {
  display: flex;
  justify-content: space-around;
  align-items: center;
  gap: 20px;
}

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

.card {
  border-radius: 15px;
  padding: 2.5rem;
  background: rgba(255, 255, 255, 0.9);
  box-shadow: 0 6px 30px rgba(0, 0, 0, 0.15);
}
</style>
