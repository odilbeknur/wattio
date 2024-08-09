var columnChart, columnChartoptions = {
        series: [{
            name: "Orders",
            data: [32, 66, 44, 55, 41, 24, 67, 22, 43, 32, 66, 44, 55, 41, 24, 67, 22, 43]
        },],
        chart: {
            type: "bar",
            height: 400,
            stacked: !1,
            columnWidth: "70%",
            zoom: {
                enabled: !0
            },
            toolbar: {
                show: !1
            },
            background: "transparent"
        },
        dataLabels: {
            enabled: !1
        },
        theme: {
            mode: colors.chartTheme
        },
        responsive: [{
            breakpoint: 480,
            options: {
                legend: {
                    position: "bottom",
                    offsetX: -10,
                    offsetY: 0
                }
            }
        }],
        plotOptions: {
            bar: {
                horizontal: !1,
                columnWidth: "40%",
                radius: 30,
                enableShades: !1,
                endingShape: "rounded"
            }
        },
        xaxis: {
            type: "datetime",
            categories: ["01/01/2020 GMT", "01/02/2020 GMT", "01/03/2020 GMT", "01/04/2020 GMT", "01/05/2020 GMT", "01/06/2020 GMT", "01/07/2020 GMT", "01/08/2020 GMT", "01/09/2020 GMT", "01/10/2020 GMT", "01/11/2020 GMT", "01/12/2020 GMT", "01/13/2020 GMT", "01/14/2020 GMT", "01/15/2020 GMT", "01/16/2020 GMT", "01/17/2020 GMT", "01/18/2020 GMT"],
            labels: {
                show: !0,
                trim: !0,
                minHeight: void 0,
                maxHeight: 120,
                style: {
                    colors: colors.mutedColor,
                    cssClass: "text-muted",
                    fontFamily: base.defaultFontFamily,
                    fontSize: '5px',                }
            },
            axisBorder: {
                show: !1
            }
        },
        yaxis: {
            labels: {
                show: !0,
                trim: !1,
                offsetX: -10,
                minHeight: void 0,
                maxHeight: 120,
                style: {
                    colors: colors.mutedColor,
                    cssClass: "text-muted",
                    fontFamily: base.defaultFontFamily
                }
            }
        },
        legend: {
            position: "top",
            fontFamily: base.defaultFontFamily,
            fontWeight: 400,
            labels: {
                colors: colors.mutedColor,
                useSeriesColors: !1
            },
            markers: {
                width: 10,
                height: 10,
                strokeWidth: 0,
                strokeColor: "#fff",
                fillColors: [extend.primaryColor, extend.primaryColorLighter],
                radius: 6,
                customHTML: void 0,
                onClick: void 0,
                offsetX: 0,
                offsetY: 0
            },
            itemMargin: {
                horizontal: 10,
                vertical: 0
            },
            onItemClick: {
                toggleDataSeries: !0
            },
            onItemHover: {
                highlightDataSeries: !0
            }
        },
        fill: {
            opacity: 1,
            colors: [base.primaryColor, extend.primaryColorLighter]
        },
        grid: {
            show: !0,
            borderColor: colors.borderColor,
            strokeDashArray: 0,
            position: "back",
            xaxis: {
                lines: {
                    show: !1
                }
            },
            yaxis: {
                lines: {
                    show: !0
                }
            },
            row: {
                colors: void 0,
                opacity: .5
            },
            column: {
                colors: void 0,
                opacity: .5
            },
            padding: {
                top: 0,
                right: 0,
                bottom: 0,
                left: 0
            }
        }
    },
    columnChartCtn = document.querySelector("#columnChartM");
columnChartCtn && (columnChart = new ApexCharts(columnChartCtn, columnChartoptions)).render();


var columnChart, columnChartoptions = {
    series: [{
        name: "Orders",
        data: [32, 66, 44, 55, 41, 24, 67, 22, 43, 32, 66, 44, 55, 41, 24, 67, 22, 43]
    },],
    chart: {
        type: "bar",
        height: 400,
        stacked: !1,
        columnWidth: "70%",
        zoom: {
            enabled: !0
        },
        toolbar: {
            show: !1
        },
        background: "transparent"
    },
    dataLabels: {
        enabled: !1
    },
    theme: {
        mode: colors.chartTheme
    },
    responsive: [{
        breakpoint: 480,
        options: {
            legend: {
                position: "bottom",
                offsetX: -10,
                offsetY: 0
            }
        }
    }],
    plotOptions: {
        bar: {
            horizontal: !1,
            columnWidth: "40%",
            radius: 30,
            enableShades: !1,
            endingShape: "rounded"
        }
    },
    xaxis: {
        type: "datetime",
        categories: ["01/01/2020 GMT", "01/02/2020 GMT", "01/03/2020 GMT", "01/04/2020 GMT", "01/05/2020 GMT", "01/06/2020 GMT", "01/07/2020 GMT", "01/08/2020 GMT", "01/09/2020 GMT", "01/10/2020 GMT", "01/11/2020 GMT", "01/12/2020 GMT", "01/13/2020 GMT", "01/14/2020 GMT", "01/15/2020 GMT", "01/16/2020 GMT", "01/17/2020 GMT", "01/18/2020 GMT"],
        labels: {
            show: !0,
            trim: !0,
            minHeight: void 0,
            maxHeight: 120,
            style: {
                colors: colors.mutedColor,
                cssClass: "text-muted",
                fontFamily: base.defaultFontFamily,
                fontSize: '5px',                }
        },
        axisBorder: {
            show: !1
        }
    },
    yaxis: {
        labels: {
            show: !0,
            trim: !1,
            offsetX: -10,
            minHeight: void 0,
            maxHeight: 120,
            style: {
                colors: colors.mutedColor,
                cssClass: "text-muted",
                fontFamily: base.defaultFontFamily
            }
        }
    },
    legend: {
        position: "top",
        fontFamily: base.defaultFontFamily,
        fontWeight: 400,
        labels: {
            colors: colors.mutedColor,
            useSeriesColors: !1
        },
        markers: {
            width: 10,
            height: 10,
            strokeWidth: 0,
            strokeColor: "#fff",
            fillColors: [extend.primaryColor, extend.primaryColorLighter],
            radius: 6,
            customHTML: void 0,
            onClick: void 0,
            offsetX: 0,
            offsetY: 0
        },
        itemMargin: {
            horizontal: 10,
            vertical: 0
        },
        onItemClick: {
            toggleDataSeries: !0
        },
        onItemHover: {
            highlightDataSeries: !0
        }
    },
    fill: {
        opacity: 1,
        colors: [base.primaryColor, extend.primaryColorLighter]
    },
    grid: {
        show: !0,
        borderColor: colors.borderColor,
        strokeDashArray: 0,
        position: "back",
        xaxis: {
            lines: {
                show: !1
            }
        },
        yaxis: {
            lines: {
                show: !0
            }
        },
        row: {
            colors: void 0,
            opacity: .5
        },
        column: {
            colors: void 0,
            opacity: .5
        },
        padding: {
            top: 0,
            right: 0,
            bottom: 0,
            left: 0
        }
    }
},
columnChartCtn = document.querySelector("#columnChartY");
columnChartCtn && (columnChart = new ApexCharts(columnChartCtn, columnChartoptions)).render();


document.addEventListener('DOMContentLoaded', function () {
    const datepicker = document.getElementById('datepicker');
    const prevDateBtn = document.getElementById('prev-date');
    const nextDateBtn = document.getElementById('next-date');
    const serialNumberElement = document.getElementById('serial_number');
    const apiBaseURL = 'http://10.40.9.46:8080/data/chart/day/';

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
            console.log(apiURL)
                const response = await fetch(apiURL);
                const dataList = await response.json();
                const dataresponse = dataList.data_list;
                console.log(dataresponse)
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




