document.addEventListener("DOMContentLoaded", function() {
    let datepicker = document.getElementById('datepicker');

    // Initialize Flatpickr for day by default
    flatpickr(datepicker, {
        dateFormat: "Y-m-d"
    });

    document.querySelectorAll('a[data-toggle="pill"]').forEach(tab => {
        tab.addEventListener('shown.bs.tab', function (e) {
            // Destroy the current flatpickr instance
            if (datepicker._flatpickr) {
                datepicker._flatpickr.destroy();
            }
            
            // Initialize Flatpickr based on the selected tab
            if (e.target.id === 'day-tab') {
                flatpickr(datepicker, { dateFormat: "Y-m-d" });
            } else if (e.target.id === 'month-tab') {
                flatpickr(datepicker, { dateFormat: "Y-m", plugins: [new monthSelectPlugin({ shorthand: true, dateFormat: "Y-m", theme: "light" })] });
            } else if (e.target.id === 'year-tab') {
                flatpickr(datepicker, { dateFormat: "Y", plugins: [new yearSelectPlugin()] });
            }
        });
    });
});