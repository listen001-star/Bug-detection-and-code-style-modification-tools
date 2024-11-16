<template>
  <div class="chart-container">
    <Line :data="chartData" :options="chartOptions" />
  </div>
</template>

<script>
import { Line } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement } from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement);

export default {
  name: 'LineChart',
  components: {
    Line,
  },
  props: {
    data: {
      type: Object,
      required: true,
    },
  },
  computed: {
    chartData() {
      return this.data;
    },
    chartOptions() {
      return {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: true,
          },
          tooltip: {
            enabled: true,
          },
        },
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      };
    },
  },
};
</script>

<style scoped>
.chart-container {
  position: relative;
  height: 300px;
  width: 100%;
}
</style>
