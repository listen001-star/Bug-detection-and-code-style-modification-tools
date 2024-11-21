<template>
  <div class="chart-container">
    <Pie :data="chartData" :options="chartOptions" />
  </div>
  
</template>

<script>
import { Pie } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement } from 'chart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';

ChartJS.register(Title, Tooltip, Legend, ArcElement, ChartDataLabels);

export default {
  name: 'PieChart',
  components: {
    Pie,
  },
  props: {
    data: {
      type: Array,
      default: () => [20, 25, 15, 20], // 默认数据
    },
  },
  computed: {
    chartData() {
      return {
        labels: ['Error Type C', 'Error Type R', 'Error Type W', 'Error Type E'],
        datasets: [
          {
            data: this.data,
            backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0'],
          },
        ],
      };
    },
    chartOptions() {
      return {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          datalabels: {
            color: '#fff',
            formatter: (value) => `${value}%`, // 数据标签格式
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
