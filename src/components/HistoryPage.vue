<template>
  <div class="p-5">
    <h2>History Data</h2>
    <ul>
      <li v-for="file in files" :key="file.name" class="mb-3">
        <span>{{ file.name }}</span>
        <button class="btn btn-view-result ml-3" @click="viewFile(file)">查看结果</button>
      </li>
    </ul>

    <div v-if="showLineChart" class="mt-5">
      <h3>{{ selectedFile.name }} - Test Scores Over Time</h3>
      <LineChart :data="lineChartData" />

      <ul v-for="(detail, index) in selectedFile.details" :key="index" class="mt-4">
        <li class="mb-3">
          <span>Test {{ index + 1 }}: Score {{ detail.score }}</span>
          <button class="btn btn-view-detail ml-3" @click="viewDetail(detail)">查看详情</button>
        </li>
      </ul>
    </div>

    <!-- 弹窗显示详细数据 -->
    <div v-if="showDetailModal" class="modal-overlay">
      <div class="modal-content">
        <h3>Test Detail</h3>
        <p>Score: {{ detailData.score }}</p>
        <PieChart :data="detailData.pieData" />
        <BarChart :data="detailData.barData" />
        <button class="btn btn-close-modal mt-3" @click="closeDetailModal">Close</button>
      </div>
    </div>
  </div>
</template>

<script>
import LineChart from './LineChart.vue';
import PieChart from './PieChart.vue';
import BarChart from './BarChart.vue';

export default {
  name: 'HistoryPage',
  components: {
    LineChart,
    PieChart,
    BarChart,
  },
  data() {
    function generateRandomTestData() {
      return {
        score: Math.floor(Math.random() * 30) + 70, // 随机分数在70-100之间
        pieData: Array.from({ length: 5 }, () => Math.floor(Math.random() * 25) + 10), // 随机饼图数据
        barData: Array.from({ length: 5 }, () => Math.floor(Math.random() * 40) + 20), // 随机柱状图数据
      };
    }

    return {
      files: [
        {
          name: 'analysis1.py',
          details: Array.from({ length: 10 }, generateRandomTestData),
        },
        {
          name: 'analysis2.py',
          details: Array.from({ length: 10 }, generateRandomTestData),
        },
      ],
      defaultFiles: [
        {
          name: 'analysis1.py',
          details: Array.from({ length: 10 }, generateRandomTestData),
        },
        {
          name: 'analysis2.py',
          details: Array.from({ length: 10 }, generateRandomTestData),
        },
      ],
      showLineChart: false,
      showDetailModal: false,
      selectedFile: null,
      detailData: {},
    };
  },
  computed: {
    lineChartData() {
      if (!this.selectedFile) return {};
      return {
        labels: this.selectedFile.details.map((_, index) => `Test ${index + 1}`),
        datasets: [
          {
            label: 'Score',
            data: this.selectedFile.details.map(detail => detail.score),
            borderColor: '#36A2EB',
            fill: false,
          },
        ],
      };
    },
  },
  methods: {
    async fetchHistory() {
      try {
        const response = await fetch('http://127.0.0.1:8000/file/history/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ filename: 'all' }),
        });

        if (response.ok) {
          const data = await response.json();
          if (data.success && data.data) {
            this.files = data.data.map(item => ({
              name: item.file_name,
              details: item.file_report.map(() => ({
                score: Math.floor(Math.random() * 30) + 70, // 模拟分数
                pieData: Array.from({ length: 5 }, () => Math.floor(Math.random() * 25) + 10),
                barData: Array.from({ length: 5 }, () => Math.floor(Math.random() * 40) + 20),
              })),
            }));
          } else {
            console.warn('No data in response. Using default files.');
            this.files = this.defaultFiles;
          }
        } else {
          console.error('Failed to fetch history. Using default files.');
          this.files = this.defaultFiles;
        }
      } catch (error) {
        console.error('Error while fetching history:', error);
        this.files = this.defaultFiles;
      }
    },
    viewFile(file) {
      this.selectedFile = file;
      this.showLineChart = true;
    },
    viewDetail(detail) {
      this.detailData = detail;
      this.showDetailModal = true;
    },
    closeDetailModal() {
      this.showDetailModal = false;
    },
  },
  created() {
    this.fetchHistory();
  },
};
</script>

<style scoped>
.btn-view-result, .btn-view-detail {
  background: #5bc0de;
  color: #fff;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 8px;
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
</style>
