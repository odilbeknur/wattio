document.addEventListener('DOMContentLoaded', function () {
    const datepicker = document.getElementById('datepicker');
    const dayBtn = document.getElementById('day-btn');
    const monthBtn = document.getElementById('month-btn');
    const yearBtn = document.getElementById('year-btn');
    const prevDateBtn = document.getElementById('prev-date');
    const nextDateBtn = document.getElementById('next-date');
    const apiBaseURL = '/api/fetch-data/';

    // Initialize Flatpickr with today's date as default
    const fp = flatpickr(datepicker, {
        dateFormat: "Y-m-d",
        defaultDate: new Date(),
        onChange: fetchDataAndUpdateChart
    });
    prevDateBtn.addEventListener('click', function () {
        navigateDate(-1);
    });

    nextDateBtn.addEventListener('click', function () {
        navigateDate(1);
    });

    function setActiveButton(button) {
        document.querySelectorAll('.date-btn').forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');
    }

    function navigateDate(direction) {
        const currentDate = fp.selectedDates[0] || new Date();
        let newDate;

        newDate = new Date(currentDate.setDate(currentDate.getDate() + direction));
        fp.set('dateFormat', 'Y-m-d');
       

        fp.setDate(newDate);
        fetchDataAndUpdateChart();
    }

    async function fetchDataAndUpdateChart() {
      const dateValue = datepicker.value;
      if (dateValue) {
          let interval;
          if (dayBtn.classList.contains('active')) {
              interval = 'day';
          } else if (monthBtn.classList.contains('active')) {
              interval = 'month';
          } else if (yearBtn.classList.contains('active')) {
              interval = 'year';
          }

          const apiURL = `${apiBaseURL}?start_date=${dateValue}&interval=${interval}`;
          const response = await fetch(apiURL);
          const data = await response.json();
          updateChart(data);

          console.log(data)
      }
  }

    let chartInstance;

    function updateChart(dataList) {
        const ctx2 = document.getElementById("chart-line").getContext("2d");

        if (chartInstance) {
            chartInstance.destroy(); // Destroy existing chart instance if it exists
        }

        const gradientStroke1 = ctx2.createLinearGradient(0, 230, 0, 50);
        gradientStroke1.addColorStop(1, 'rgba(75, 192, 192, 0.2)');
        gradientStroke1.addColorStop(0.2, 'rgba(75, 192, 192, 0.0)');
        gradientStroke1.addColorStop(0, 'rgba(75, 192, 192, 0)');

        chartInstance = new Chart(ctx2, {
            type: "line",
            data: {
                labels: dataList.labels, // Map the time from data_list
                datasets: [{
                    label: "IES",
                    tension: 0.4,
                    borderWidth: 0,
                    pointRadius: 0,
                    borderColor: "#4bc0c0",
                    borderWidth: 3,
                    backgroundColor: gradientStroke1,
                    fill: true,
                    data: dataList.data, // Map the values from data_list
                    maxBarThickness: 6
                }],
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: true,
                    }
                },
                interaction: {
                    intersect: false,
                    mode: 'index',
                },
                scales: {
                    y: {
                        grid: {
                            drawBorder: true,
                            display: true,
                            drawOnChartArea: true,
                            drawTicks: true,
                            borderDash: [5, 5]
                        },
                        ticks: {
                            display: true,
                            padding: 10,
                            color: '#b2b9bf',
                            font: {
                                size: 11,
                                family: "Open Sans",
                                style: 'normal',
                                lineHeight: 2
                            },
                        }
                    },
                    x: {
                        grid: {
                            drawBorder: true,
                            display: true,
                            drawOnChartArea: false,
                            drawTicks: true,
                            borderDash: [5, 5]
                        },
                        ticks: {
                            display: true,
                            color: '#b2b9bf',
                            padding: 20,
                            font: {
                                size: 11,
                                family: "Open Sans",
                                style: 'normal',
                                lineHeight: 2
                            },
                        }
                    },
                },
            },
        });
    }

    // Initialize chart with default data (if needed)
    fetchDataAndUpdateChart();
});