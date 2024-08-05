var columnChart, columnChartoptions = {
        series: [{
            name: "Orders",
            data: [32, 66, 44, 55, 41, 24, 67, 22, 43, 32, 66, 44, 55, 41, 24, 67, 22, 43]
        }, {
            name: "Visitors",
            data: [7, 30, 13, 23, 20, 12, 8, 13, 27, 7, 30, 13, 23, 20, 12, 8, 13, 27]
        }],
        chart: {
            type: "bar",
            height: 350,
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
    columnChartCtn = document.querySelector("#columnChart");
columnChartCtn && (columnChart = new ApexCharts(columnChartCtn, columnChartoptions)).render();

document.addEventListener('DOMContentLoaded', function () {
    const datepicker = document.getElementById('datepicker');
    const todayDateBtn = document.getElementById('today-btn');
    const prevDateBtn = document.getElementById('prev-date');
    const nextDateBtn = document.getElementById('next-date');
    const apiBaseURL = '/api/fetch-data/';

    // Initialize Flatpickr with today's date as default
    const fp = flatpickr(datepicker, {
        dateFormat: "Y-m-d",
        defaultDate: new Date(),
        onChange: fetchDataAndUpdateChart
    });

    prevDateBtn.addEventListener('click', function (event) {
        event.preventDefault();
        navigateDate(-1);
    });

    nextDateBtn.addEventListener('click', function (event) {
        event.preventDefault();
        navigateDate(1);
    });

    function setActiveButton(button) {
        document.querySelectorAll('.date-btn').forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');
    }

    function navigateDate(direction) {
        const currentDate = fp.selectedDates[0] || new Date();
        let newDate = new Date(currentDate.setDate(currentDate.getDate() + direction));
        fp.setDate(newDate);
        fetchDataAndUpdateChart();
    }

    var lineChart, lineChartoptions = {
        series: [{
            name: "Sozlash",
            data: [] // Empty array initially
        }],
        chart: {
            height: 400,
            type: "line",
            background: !1,
            zoom: {
                enabled: 1
            },
            toolbar: {
                show: 1
            }
        },
        theme: {
            mode: colors.chartTheme
        },
        stroke: {
            show: !0,
            curve: "smooth",
            lineCap: "round",
            colors: chartColors,
            width: [3, 2, 3],
            dashArray: [0, 0, 0]
        },
        dataLabels: {
            enabled: !1
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
        markers: {
            size: 4,
            colors: base.primaryColor,
            strokeColors: colors.borderColor,
            strokeWidth: 2,
            strokeOpacity: .9,
            strokeDashArray: 0,
            fillOpacity: 1,
            discrete: [],
            shape: "circle",
            radius: 2,
            offsetX: 0,
            offsetY: 0,
            onClick: void 0,
            onDblClick: void 0,
            showNullDataPoints: !0,
            hover: {
                size: void 0,
                sizeOffset: 3
            }
        },
        xaxis: {
            type: "datetime",
            categories: [],
            labels: {
                show: !0,
                trim: !1,
                minHeight: void 0,
                maxHeight: 120,
                style: {
                    colors: colors.mutedColor,
                    cssClass: "text-muted",
                    fontFamily: base.defaultFontFamily
                }
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
                strokeColor: colors.borderColor,
                fillColors: chartColors,
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
    };

    async function fetchDataAndUpdateChart() {
        const dateValue = fp.selectedDates[0].toISOString().split('T')[0];
        
        if (dateValue) {
            const apiURL = `${apiBaseURL}?start_date=${dateValue}`;
            const response = await fetch(apiURL);
            const dataList = await response.json();
            console.log(dataList)
            // Check if dataList contains labels and data
            if (dataList.labels && dataList.data) {
                const lineChartCtn = document.querySelector("#lineChart");
                if (lineChartCtn) {
                    // Update chart options
                    const updatedOptions = {
                        ...lineChartoptions,
                        series: [{
                            name: "Sozlash",
                            data: dataList.data
                        }],
                        xaxis: {
                            categories: dataList.labels
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
                console.error('Invalid data format:', dataList);
            }
        }
    }

    // Initial chart rendering
    fetchDataAndUpdateChart();
});
