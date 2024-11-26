<template>
  <div class="p-5">
    <h2>History Data</h2>
    <ul>
      <li v-for="file in files" :key="file.name" class="mb-3">
        <span>{{ file.name }}  </span>
        <button class="btn btn-view-result ml-5" @click="viewFile(file)">View Result</button>
      </li>
    </ul>

    <div v-if="showLineChart" class="mt-5">
      <h3>{{ selectedFile.name }} - Test Scores Over Time</h3>
      <LineChart :data="lineChartData" />

      <ul v-for="(detail, index) in selectedFile.details" :key="index" class="mt-4">
        <li class="mb-3">
          <span>Test {{ index + 1 }}: Score {{ detail.score }}</span>
          <button class="btn btn-view-detail ml-5" @click="viewDetail(detail)">View Details</button>
        </li>
      </ul>
    </div>

    <!-- Modal to show detailed data -->
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
    return {
      defaultData: {
        success: true,
        data: [
          {
            id: 1,
            user_id: 1,
            file_name: "test",
            file_content: "xxxxxx",
            file_c: 7,
            file_w: 5,
            file_e: 3,
            file_r: 0,
            file_score: 0,
            file_date: "2024-11-13T15:19:29Z",
          },
          {
            id: 2,
            user_id: 1,
            file_name: "test",
            file_content: "xxxxxx",
            file_c: 9,
            file_w: 5,
            file_e: 4,
            file_r: 0,
            file_score: 0,
            file_date: "2024-11-13T15:25:39Z",
          },
          {
            id: 3,
            user_id: 1,
            file_name: "test",
            file_content: "xxxxxx",
            file_c: 8,
            file_w: 5,
            file_e: 4,
            file_r: 0,
            file_score: 0,
            file_date: "2024-11-13T15:25:58Z",
          },
          {
            id: 4,
            user_id: 1,
            file_name: "111.py",
            file_content: "111.py",
            file_c: 4,
            file_w: 0,
            file_e: 1,
            file_r: 0,
            file_score: 5,
            file_date: "2024-11-14T00:02:17Z",
          },
          {
            id: 5,
            user_id: 1,
            file_name: "111.py",
            file_content:
              "b'\\r\\nimport pandas as pd\\r\\nfrom sklearn.model_selection import train_test_split\\r\\nfrom sklearn.preprocessing import LabelEncoder\\r\\nimport tensorflow as tf\\r\\n\\r\\n# Step 1: Load the data\\r\\ndata = pd.read_csv(r\\'C:\\\\Users\\\\15825\\\\Desktop\\\\CS5481Data  Engineering\\\\assignment\\\\assignment2\\\\ratings.csv\\')\\r\\n\\r\\n# Display the first few rows of the original dataset\\r\\nprint(\"Original Data:\")\\r\\nprint(data.head())\\r\\n\\r\\n# Step 2: Encode user_id and book_id to integers\\r\\nuser_encoder = LabelEncoder()\\r\\nbook_encoder = LabelEncoder()\\r\\n\\r\\ndata[\\'user_id\\'] = user_encoder.fit_transform(data[\\'user_id\\'])\\r\\ndata[\\'book_id\\'] = book_encoder.fit_transform(data[\\'book_id\\'])\\r\\n\\r\\n# Step 3: Create the user-item interaction matrix\\r\\nuser_item_matrix = data.pivot(index=\\'user_id\\', columns=\\'book_id\\', values=\\'rating\\').fillna(0)\\r\\n\\r\\n# Convert the matrix to a NumPy array\\r\\nuser_item_matrix_np = user_item_matrix.values\\r\\n\\r\\n# Step 4: Split the data into training and test sets\\r\\ntrain_data, test_data = train_test_split(user_item_matrix_np, test_size=0.2, random_state=42)\\r\\n\\r\\n# Convert the training and test data to TensorFlow tensors\\r\\ntrain_data_tensor = tf.convert_to_tensor(train_data, dtype=tf.float32)\\r\\ntest_data_tensor = tf.convert_to_tensor(test_data, dtype=tf.float32)\\r\\n\\r\\n# Display the first 5 processed entries of the user-item matrix\\r\\nprint(\"Processed User-Item Matrix (First 5 Entries):\")\\r\\nprint(user_item_matrix.head())\\r\\n\\r\\n\\r\\n'",
            file_c: 4,
            file_w: 0,
            file_e: 1,
            file_r: 0,
            file_score: 5,
            file_date: "2024-11-14T00:05:53Z",
          },
        ],
      },
      files: [], // Used to store structured file data
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
        labels: this.selectedFile.details.map((_, index) => `Test ${index + 1}`), // X-axis is the test number
        datasets: [
          {
            label: 'Score',
            data: this.selectedFile.details.map(detail => detail.score), // Y-axis is the score
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
            // Categorize files by file_name
            const files = data.data.reduce((acc, item) => {
              const existingFile = acc.find(f => f.name === item.file_name);
              const total = item.file_c + item.file_w + item.file_e + item.file_r;
              const newDetail = {
                score: item.file_score,
                barData: [item.file_c, item.file_w, item.file_e, item.file_r],
                pieData: total === 0 ? [0, 0, 0, 0] : [
                  ((item.file_c / total) * 100).toFixed(2),
                  ((item.file_w / total) * 100).toFixed(2),
                  ((item.file_e / total) * 100).toFixed(2),
                  ((item.file_r / total) * 100).toFixed(2),
                ], // Calculate pie chart proportions
              };

              if (existingFile) {
                existingFile.details.push(newDetail);
              } else {
                acc.push({
                  name: item.file_name,
                  details: [newDetail],
                });
              }
              return acc;
            }, []);
            this.files = files;
          } else {
            console.warn("No data in response. Using default files.");
            this.loadDefaultFiles();
          }
        } else {
          console.error("Failed to fetch history. Using default files.");
          this.loadDefaultFiles();
        }
      } catch (error) {
        console.error("Error while fetching history:", error);
        this.loadDefaultFiles();
      }
    },
    loadDefaultFiles() {
      const files = this.defaultData.data.reduce((acc, item) => {
        const existingFile = acc.find(f => f.name === item.file_name);
        const total = item.file_c + item.file_w + item.file_e + item.file_r;
        const newDetail = {
          score: item.file_score,
          barData: [item.file_c, item.file_w, item.file_e, item.file_r],
          pieData: total === 0 ? [0, 0, 0, 0] : [
            ((item.file_c / total) * 100).toFixed(2),
            ((item.file_w / total) * 100).toFixed(2),
            ((item.file_e / total) * 100).toFixed(2),
            ((item.file_r / total) * 100).toFixed(2),
          ],
        };

        if (existingFile) {
          existingFile.details.push(newDetail);
        } else {
          acc.push({
            name: item.file_name,
            details: [newDetail],
          });
        }
        return acc;
      }, []);
      this.files = files;
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
