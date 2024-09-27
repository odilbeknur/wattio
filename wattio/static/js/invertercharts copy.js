document.addEventListener('DOMContentLoaded', function () {
    const apiColumnURL = 'http://10.20.6.30:8080/data/chart/month/';
    const chartColors = ["#008FFB", "#00E396", "#FEB019", "#FF4560", "#775DD0", "#3F51B5", "#03A9F4", "#4CAF50", "#F9CE1D", "#FF9800"];
    const serialNumberElement = document.getElementById('serial_number');
    const serialNumber = serialNumberElement ? serialNumberElement.textContent : '';

    if (!serialNumber) {
        console.error('Серийный номер не найден на странице.');
        return;
    }

    // Initialize Flatpickr for month selection
    const fp = flatpickr("#monthpicker", {
        plugins: [
            new monthSelectPlugin({
                shorthand: true,
                dateFormat: "Y/m",
                theme: "light"
            })
        ],
        minDate: "2024-09", 
        defaultDate: new Date(),
        onChange: function() {
            if (fp.selectedDates.length > 0) {
                fetchDataAndUpdateColumnChart(); // Fetch data whenever the date changes
            }
        }
    });

    let columnChart;

    // Initial chart options
    const columnChartOptions = {
        chart: {
            type: "bar",
            height: 400,
            stacked: false,
            columnWidth: "40%", // Оставляем одно значение
            zoom: {
                enabled: false
            },
            toolbar: {
                show: false
            },
            background: "transparent"
        },
        dataLabels: {
            enabled: false
        },
        fill: {
            opacity: 1,
            colors: chartColors
        },
        plotOptions: {
            bar: {
                horizontal: false,
                columnWidth: "40%", // Оставляем одно значение
                radius: 30,
                enableShades: false,
                endingShape: "rounded"
            }
        },
        xaxis: {
            type: "datetime",
            labels: {
                show: true,
                style: {
                    colors: "#8e8da4",
                    fontSize: '5px',
                }
            },
            axisBorder: {
                show: false
            }
        },
        yaxis: {
            labels: {
                show: true,
                formatter: function (val) {
                    return val + " кВт"; // Append 'кВт' to the Y-axis values
                }
            }
        },
        legend: {
            position: "top",
            markers: {
                width: 10,
                height: 10,
                radius: 6
            }
        },
        grid: {
            show: true,
            borderColor: "#e0e0e0",
            yaxis: {
                lines: {
                    show: true
                }
            }
        }
    };

    function formatDate(date) {
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0');
        return `${year}/${month}`; // Format as "YYYY/MM"
    }

    async function fetchDataAndUpdateColumnChart() {
        if (!fp.selectedDates[0]) {
            console.warn('Дата не выбрана.');
            return;
        }
    
        const monthValue = formatDate(fp.selectedDates[0]);
        const apiURL = `${apiColumnURL}${serialNumber}/${monthValue}`;
    
        try {
            const response = await fetch(apiURL);
            if (!response.ok) {
                throw new Error('Ошибка сети: ' + response.statusText);
            }
    
            const data = await response.json();
    
            // Проверка, что data_list существует и является массивом
            if (data && Array.isArray(data.data_list) && data.data_list.length > 0) {
                const seriesData = [{
                    name: serialNumber,
                    data: data.data_list.map(dataItem => {
                        let date = new Date(dataItem.create_date);
                        date.setHours(date.getHours() + 5); // Adjust for timezone
                        return {
                            x: date.getTime(),
                            y: dataItem.data
                        };
                    }),
                    color: chartColors[0] // Если несколько серий, можно добавить разные цвета
                }];
    
                const columnChartContainer = document.querySelector("#columnChartM");
                if (columnChartContainer) {
                    const updatedOptions = {
                        ...columnChartOptions,
                        series: seriesData,
                        legend: {
                            ...columnChartOptions.legend,
                            markers: {
                                fillColors: seriesData.map(s => s.color),
                            }
                        }
                    };
    
                    if (columnChart) {
                        columnChart.destroy();
                    }
    
                    columnChart = new ApexCharts(columnChartContainer, updatedOptions);
                    columnChart.render();
                }
            } else {
                console.warn('Нет данных для выбранного месяца или data_list не является массивом.');
                // Дополнительное уведомление для пользователя
            }
        } catch (error) {
            console.error('Ошибка при получении или разборе данных:', error);
        }
    }
    
    fetchDataAndUpdateColumnChart();
});


document.addEventListener('DOMContentLoaded', function () {
    const datepicker = document.getElementById('datepicker');
    const prevDateBtn = document.getElementById('prev-date');
    const nextDateBtn = document.getElementById('next-date');
    const serialNumberElement = document.getElementById('serial_number');
    const apiBaseURL = 'http://10.20.6.30:8080/data/chart/day/';

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

    function navigateDate(direction) {
        const currentDate = fp.selectedDates[0] || new Date();
        const newDate = new Date(currentDate.setDate(currentDate.getDate() + direction));
        fp.setDate(newDate);
        fetchDataAndUpdateChart();
    }

    const chartColors = ["#008FFB", "#00E396", "#FEB019", "#FF4560", "#775DD0", "#3F51B5", "#03A9F4", "#4CAF50", "#F9CE1D", "#FF9800"];

    var lineChart, lineChartoptions = {
        series: [], // Initialize with empty array
        chart: {
            height: 400,
            type: "line",
            background: false,
            zoom: {
                enabled: false
            },
            toolbar: {
                show: true
            }
        },
        stroke: {
            show: true,
            curve: "smooth",
            lineCap: "round",
            colors: chartColors,
            width: [3, 2, 3],
            dashArray: [0, 0, 0]
        },
        dataLabels: {
            enabled: false
        },
        markers: {
            size: 4,
            colors: chartColors,
            strokeColors: '#fff',
            strokeWidth: 2,
            strokeOpacity: 0.9,
            strokeDashArray: 0,
            fillOpacity: 1,
            discrete: [],
            shape: "circle",
            radius: 2,
            offsetX: 0,
            offsetY: 0,
            showNullDataPoints: true,
            hover: {
                size: undefined,
                sizeOffset: 3
            }
        },
        xaxis: {
            type: "datetime",
            labels: {
                show: false,
                formatter: function(value, timestamp) {
                    const date = new Date(timestamp);
                    const hours = date.getHours();
                    const minutes = date.getMinutes();
                    return `${hours}:${minutes < 10 ? '0' : ''}${minutes}`;
                },
                style: {
                    colors: '#333',
                    cssClass: "text-muted",
                    fontFamily: 'Arial'
                }
            },
            axisBorder: {
                show: false
            }
        },
        yaxis: {
            labels: {
                show: true,
                trim: false,
                offsetX: -10,
                maxHeight: 120,
                style: {
                    colors: '#333',
                    cssClass: "text-muted",
                    fontFamily: 'Arial'
                }
            }
        },
        legend: {
            position: "top",
            fontFamily: 'Arial',
            fontWeight: 400,
            labels: {
                colors: '#333',
                useSeriesColors: false
            },
            markers: {  
                width: 10,
                height: 10,
                strokeWidth: 0,
                strokeColor: '#fff',
                fillColors: chartColors,
                radius: 6,
                offsetX: 0,
                offsetY: 0
            },
            itemMargin: {
                horizontal: 10,
                vertical: 0
            },
            onItemClick: {
                toggleDataSeries: true
            },
            onItemHover: {
                highlightDataSeries: true
            }
        },
        grid: {
            show: true,
            borderColor: '#e7e7e7',
            strokeDashArray: 0,
            position: "back",
            xaxis: {
                lines: {
                    show: false
                }
            },
            yaxis: {
                lines: {
                    show: true
                }
            },
            row: {
                colors: undefined,
                opacity: 0.5
            },
            column: {
                colors: undefined,
                opacity: 0.5
            },
            padding: {
                top: 0,
                right: 0,
                bottom: 0,
                left: 0
            }
        }
    };

    function formatDate(date) {
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');
        return `${year}-${month}-${day}`;
    }

    async function fetchDataAndUpdateChart() {
        const dateValue = formatDate(fp.selectedDates[0]);
        const serialNumber = serialNumberElement ? serialNumberElement.textContent : '';
        if (dateValue && serialNumber) {
            const apiURL = `${apiBaseURL}${serialNumber}/${dateValue}`;
                const response = await fetch(apiURL);
                const dataList = await response.json();
                const dataresponse = dataList.data_list;
                if (dataresponse.length > 0) {
                    const seriesData = [{
                        name: serialNumber,
                        data: dataresponse.map(dataItem => {
                            let dates = new Date(dataItem.create_date);
                            dates.setHours(dates.getHours() + 5);
                            return {
                                x: dates.getTime(),
                                y: dataItem.data
                            };
                        }),
                        color: chartColors[0] // Assuming one color for one series
                    }];
                    const lineChartCtn = document.querySelector("#lineChart");
                    if (lineChartCtn) {
                        // Update chart options
                        const updatedOptions = {
                            ...lineChartoptions,
                            series: seriesData,
                            markers: {
                                ...lineChartoptions.markers,
                                colors: [chartColors[0]]
                            }
                        };
                        
                        // Destroy the previous chart instance if it exists
                        if (lineChart) {
                            lineChart.destroy();
                        }
                
                        // Create and render a new chart
                        lineChart = new ApexCharts(lineChartCtn, updatedOptions);
                        lineChart.render();
                    }
                } else {
                    console.error('Нет данных для выбранной даты.');
                    // Destroy the previous chart instance if it exists
                    if (lineChart) {
                        lineChart.destroy();
                        lineChart = null; // Clear the reference to the chart instance
                    }
                
                    // Clear the chart container
                    const lineChartCtn = document.querySelector("#lineChart");
                    if (lineChartCtn) {
                        lineChartCtn.innerHTML = '<p>Нет данных для выбранной даты.</p>';
                    }
                }
                
        }
    }

    // Initial chart rendering
    fetchDataAndUpdateChart();
});




