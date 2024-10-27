<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <div class="card p-4 shadow rounded">
          <h2 class="text-center mb-4">Welcome to Main Page</h2>

          <div class="mb-3">
            <h3>Upload Python File</h3>
            <input type="file" class="form-control-file" accept=".py" @change="handleFileUpload" />
          </div>

          <div class="mb-3">
            <h3>Execute Command</h3>
            <button class="btn btn-info" @click="executeCommand" :disabled="!uploadedFile">Analyze with Pylint</button>
          </div>

          <div v-if="analysisResult" class="mt-3">
            <h3>Results</h3>
            <pre class="result-box">{{ analysisResult }}</pre>
          </div>

          <div v-if="downloadLink" class="mt-3">
            <a :href="downloadLink" class="btn btn-success" download>Download Result File</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MainPage',
  data() {
    return {
      uploadedFile: null,
      analysisResult: null,
      downloadLink: null,
    };
  },
  methods: {
    handleFileUpload(event) {
      this.uploadedFile = event.target.files[0];
      this.analysisResult = null;
      this.downloadLink = null;
    },
    async executeCommand() {
      if (!this.uploadedFile) {
        alert('Please upload a file first.');
        return;
      }

      // Create a FormData object to send the file
      const formData = new FormData();
      formData.append('file', this.uploadedFile);

      try {
        // Sending the file to the backend for analysis
        const response = await fetch('http://your-backend-url/api/analyze', {
          method: 'POST',
          body: formData,
        });

        if (!response.ok) {
          throw new Error('Failed to analyze the file.');
        }

        const data = await response.json();
        this.analysisResult = data.result;

        // Create a download link for the result file
        const blob = new Blob([data.result], { type: 'text/plain' });
        this.downloadLink = URL.createObjectURL(blob);
      } catch (error) {
        alert(`Error: ${error.message}`);
        console.error(error);
      }
    },
  },
};
</script>

<style scoped>
.container {
  margin-top: 50px;
}

.card {
  border-radius: 15px;
  background: rgba(255, 255, 255, 0.85);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
}

h2, h3 {
  color: #333;
}

.btn-info {
  background: linear-gradient(to right, #56ccf2, #2f80ed);
  border: none;
  transition: all 0.3s ease;
}

.btn-info:hover {
  background: linear-gradient(to right, #499ecf, #276cb5);
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
</style>
