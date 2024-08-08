document.addEventListener('DOMContentLoaded', function () {
    $('.modal-shortcut').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget); // Button that triggered the modal
        var name = button.data('name'); 
        var model = button.data('model');
        var serial = button.data('serial');
        var totalEnergy = button.data('total-energy');
        var workTime = button.data('work-time');
        var todayEnergy = button.data('today-generate-energy');
        var temperature = button.data('temperature'); 
        var currentPower = button.data('current-power');
        var status = button.data('status');
        
        
        // Update the modal's content
        var modal = $(this);
        modal.find('#modalName').text(name);
        modal.find('#modalModel').text(model);
        modal.find('#modalSerial').text(serial);
        modal.find('#modalTotalEnergy').text(totalEnergy + ' кВт·ч');
        modal.find('#modalTodayEnergy').text(todayEnergy + ' Вт·ч');
        modal.find('#modalTemperature').text(temperature + ' ℃');
        modal.find('#modalCurrentPower').text(currentPower + ' Вт');
        modal.find('#modalTotalEnergy').text(totalEnergy + ' кВт·ч');
        modal.find('#modalWorkTime').text(workTime + ' ч');
        
        // Set status text based on status value
        var statusText = '';
        var statusClass = '';
        if (status == '1') {
            statusText = 'Online';
            statusClass = 'text-success';
        } else if (status == '0') {
            statusText = 'Waiting';
            statusClass = 'text-secondary';
        } else if (status == '3') {
            statusText = 'Fault';
            statusClass = 'text-danger';
        }
        modal.find('#modalStatus').html('<span class="' + statusClass + '">' + statusText + '</span>');
       
       // Construct the URL dynamically
       var baseUrl = "{% url 'inverter' dummy_serial %}";  // Generates a URL like /inverter/dummy_serial/
       var detailUrl = baseUrl.replace('dummy_serial', serial);  // Replaces 'dummy_serial' with the actual serial number

       var modalLink = document.getElementById('modalLink');
            modalLink.href = '/inverter/' + serial;
    });
});