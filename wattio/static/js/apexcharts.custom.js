document.addEventListener('DOMContentLoaded', function () {
    const chartColors = ["#008FFB", "#00E396", "#FEB019", "#FF4560", "#775DD0", "#3F51B5", "#03A9F4", "#4CAF50", "#F9CE1D", "#FF9800"];
    apiBaseURL = document.getElementById('plant-api').getAttribute('data-location');
       
    // Initialize Flatpickr for Month Picker
    const monthPicker = flatpickr("#monthpicker", {
        plugins: [new monthSelectPlugin({ shorthand: true, dateFormat: "Y/m", theme: "light" })],
        minDate: "2024-09",
        defaultDate: new Date(),
        onChange: fetchDataAndUpdateColumnChart
    });

    // Initialize Flatpickr for Date Picker
    const datePicker = flatpickr("#datepicker", {
        dateFormat: "Y-m-d",
        defaultDate: new Date(),
        onChange: fetchDataAndUpdateChart
    });

    // Event listeners for navigating dates
    document.getElementById('prev-date').addEventListener('click', () => navigateDate(-1));
    document.getElementById('next-date').addEventListener('click', () => navigateDate(1));

    let columnChart, lineChart;
    
    const columnChartOptions = createColumnChartOptions();
    const lineChartOptions = createLineChartOptions();

    function createColumnChartOptions() {
        return {
            chart: { type: "bar", height: 400, stacked: false, columnWidth: "70%", zoom: { enabled: false }, toolbar: { show: false }, background: "transparent" },
            dataLabels: { enabled: false },
            responsive: [{ breakpoint: 480, options: { legend: { position: "bottom", offsetX: -10, offsetY: 0 } } }],
            plotOptions: { bar: { horizontal: false, columnWidth: "40%", radius: 30, enableShades: false, endingShape: "rounded" } },
            xaxis: { type: "datetime", labels: { show: false, style: { colors: '#555', fontFamily: 'Arial', fontSize: '10px' } } },
            yaxis: { labels: { show: true, formatter: val => val + " кВт" } },
            legend: { position: "top", markers: { fillColors: chartColors } },
            fill: { opacity: 1, colors: chartColors },
            grid: { show: true },
            tooltip: { 
                x: { formatter: function(value) {
                    const date = new Date(value);
                    return date.toLocaleDateString('ru-RU', { day: 'numeric', month: 'long', year: 'numeric' });
                } },
                y: { formatter: val => val + " кВт" }
            },
        };
    }

    function createLineChartOptions() {
        return {
            series: [],
            chart: { height: 400, type: "line", background: false, zoom: { enabled: false }, toolbar: { show: true } },
            stroke: { curve: "smooth", colors: chartColors },
            dataLabels: { enabled: false },
            markers: { size: 4, colors: chartColors, strokeColors: '#fff', strokeWidth: 2 },
            xaxis: { type: "datetime", labels: { show: false, formatter: function (value, timestamp) {
                const date = new Date(timestamp);
                const hours = date.getHours();
                const minutes = date.getMinutes();
                return `${hours}:${minutes < 10 ? '0' : ''}${minutes}`;
            } } },
            yaxis: { labels: { show: true, formatter: val => val + " Вт" },   },
            legend: { position: "top", markers: { fillColors: chartColors } },
            grid: { show: true }
        };
    }

    function formatDate(date) {
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');
        return `${year}-${month}-${day}`;
    }

    async function fetchDataAndUpdateColumnChart() {
        const selectedDate = monthPicker.selectedDates[0];
        
        // Format the month to "YYYY/MM"
        const year = selectedDate.getFullYear();
        const month = String(selectedDate.getMonth() + 1).padStart(2, '0'); // Month is 0-indexed
        const monthValue = `${year}/${month}`; // Combine year and month in "YYYY/MM" format
        
        const apiURL = `${apiBaseURL}/data/chart/month/all/${monthValue}`;
        try {
            const response = await fetch(apiURL);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
    
            const dataList = await response.json();
    
            if (dataList.length > 0) {
                const seriesData = dataList.map((item, index) => ({
                    name: item.serial_number,
                    data: item.data_list.map(dataItem => {
                        let date = new Date(dataItem.create_date);
                        return { x: date.getTime(), y: dataItem.data };
                    }),
                    color: chartColors[index % chartColors.length]
                }));
    
                const columnChartContainer = document.querySelector("#columnChartM");
                if (columnChartContainer) {
                    if (columnChart) columnChart.destroy(); // Destroy the previous instance
                    columnChart = new ApexCharts(columnChartContainer, { ...columnChartOptions, series: seriesData });
                    await columnChart.render(); // Ensure the chart is rendered after initialization
                }
            } else {
                console.warn('No data available for the selected month.');
            }
        } catch (error) {
            console.error('Error fetching or parsing data:', error);
        }
    }
    

    async function fetchDataAndUpdateChart() {
        const dateValue = formatDate(datePicker.selectedDates[0]);

        console.log(dateValue)
        if (dateValue) {
            const apiURL = `${apiBaseURL}/data/chart/day/all/${dateValue}`;
            console.log(apiURL)

            try {
                const response = await fetch(apiURL);
                const dataList = await response.json();
                console.log(dataList)
                if (dataList.length > 0) {
                    const seriesData = dataList.map((item, index) => ({
                        name: item.serial_number,
                        data: item.data_list.map(dataItem => {
                            let date = new Date(dataItem.create_date);
                            date.setHours(date.getHours() + 5); // Add 5 hours to the date
                            return { x: date.getTime(), y: dataItem.data };
                        }),
                        color: chartColors[index % chartColors.length]
                    }));
                    const lineChartContainer = document.querySelector("#lineChart");
                    if (lineChartContainer) {
                        if (lineChart) lineChart.destroy(); // Destroy the previous instance
                        lineChart = new ApexCharts(lineChartContainer, { ...lineChartOptions, series: seriesData });
                        lineChart.render();
                    }
                } else {
                    console.error('No data available for the selected date.');
                }
            } catch (error) {
                console.error('Error fetching or parsing data:', error);
            }
        }
    }

    function navigateDate(direction) {
        const currentDate = datePicker.selectedDates[0] || new Date();
        const newDate = new Date(currentDate.setDate(currentDate.getDate() + direction));
        datePicker.setDate(newDate);
        fetchDataAndUpdateChart();
    }

    // Initial chart rendering
    fetchDataAndUpdateColumnChart();
    fetchDataAndUpdateChart();
});
