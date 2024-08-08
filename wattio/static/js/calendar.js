function updateDateTime() {
    const dateRangeText = document.getElementById('date-range-text');
    const currentDate = new Date();
    const dateString = currentDate.toLocaleDateString('ru-RU', { month: 'long', day: 'numeric', year: 'numeric' });
    const timeString = currentDate.toLocaleTimeString('ru-RU', { hour: 'numeric', minute: 'numeric', second: 'numeric' });
    dateRangeText.textContent = `${dateString}, ${timeString}`;
}

document.addEventListener('DOMContentLoaded', () => {
    const datePicker = document.getElementById('datepicker');
    const prevDayButton = document.getElementById('prev-date');
    const nextDayButton = document.getElementById('next-date');
    const viewButtons = document.querySelectorAll('.view-buttons .btn');
    let currentDate = new Date();

    function updateDateDisplay() {
        datePicker.value = currentDate.toISOString().substr(0, 10);
    }

    function changeDate(days) {
        currentDate.setDate(currentDate.getDate() + days);
        updateDateDisplay();
    }

    prevDayButton.addEventListener('click', () => {
        changeDate(-1);
    });

    nextDayButton.addEventListener('click', () => {
        changeDate(1);
    });

    datePicker.addEventListener('change', (e) => {
        currentDate = new Date(e.target.value);
        updateDateDisplay();
    });

    viewButtons.forEach(button => {
        button.addEventListener('click', () => {
            viewButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
        });
    });


    updateDateTime();
    updateDateDisplay();
});



