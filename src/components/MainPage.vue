<template>
  <div>
    <h2>Welcome to Main Page</h2>
    
    <!-- 上传文件 -->
    <div>
      <h3>Upload File</h3>
      <input type="file" @change="handleFileUpload" />
    </div>

    <!-- 分析按钮 -->
    <div>
      <h3>Analyze File</h3>
      <button @click="analyzeFile" :disabled="!uploadedFile">Analyze</button>
    </div>

    <!-- 可视化结果 -->
    <div v-if="analysisResult">
      <h3>Visualization of Results</h3>
      <p>{{ analysisResult }}</p>
      <!-- 您可以在此处添加更多的可视化功能 -->
    </div>
  </div>
</template>

<script>
export default {
  name: 'MainPage',
  data() {
    return {
      uploadedFile: null,
      analysisResult: null
    }
  },
  methods: {
    handleFileUpload(event) {
      this.uploadedFile = event.target.files[0];
      alert(`File ${this.uploadedFile.name} uploaded.`);
    },
    analyzeFile() {
      if (this.uploadedFile) {
        this.analysisResult = `Analysis result for ${this.uploadedFile.name}`;
      } else {
        alert('Please upload a file first.');
      }
    }
  }
}
</script>

<style scoped>
h2, h3 {
  margin-top: 20px;
}
</style>
