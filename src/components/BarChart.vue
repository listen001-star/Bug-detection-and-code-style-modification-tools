<template>
    <div class="chart-container">
      <Bar :data="chartData" :options="chartOptions" />
    </div>
  </template>
  
  <script>
  import { Bar } from 'vue-chartjs';
  import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js';
  import ChartDataLabels from 'chartjs-plugin-datalabels';

  ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, ChartDataLabels);
  
  export default {
    name: 'BarChart',
    components: {
      Bar,
    },
    props: {
      data: {
        type: Array,
        default: () => [50, 30, 40, 20, 60], // 默认的错误数量
      },
    },
    computed: {
      chartData() {
        return {
          labels: ['Error Type C', 'Error Type R', 'Error Type W', 'Error Type E', 'Error Type F'],
          datasets: [
            {
              label: 'Error Count',
              data: this.data,
              backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF'],
            },
          ],
        };
      },
      chartOptions() {
        return {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: {
              beginAtZero: true,
            },
          },
          plugins: {
            legend: {
                display: false, // 禁用图例
            },
            datalabels: {
                color: '#000',
                anchor: 'end',
                align: 'top',
            },
            title: {
                display: true,
                text: 'Error Count', // 只显示标题
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
  