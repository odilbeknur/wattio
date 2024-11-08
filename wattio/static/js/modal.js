document.addEventListener('DOMContentLoaded', function () {
    $('.modal-shortcut').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var serial = button.data('serial');


        // Parse the modalInfo JSON data
        var modalInfoData = document.getElementById('modal-info-data').textContent;
        var modalInfo = JSON.parse(modalInfoData);
        console.log(modalInfo)


        // Find the entry in modalInfo matching the serial number
        var filteredInfo = modalInfo.find(function (info) {
            return info.serial_number === serial;
        });

        var modal = $(this);
        modal.find('#modalName').text(button.data('name'));
        modal.find('#modalModel').text(button.data('model'));
        modal.find('#modalSerial').text(serial);
        modal.find('#modalTotalEnergy').text(button.data('total-energy') + ' кВт·ч');
        modal.find('#modalTodayEnergy').text(button.data('today-generate-energy') + ' кВт·ч');
        modal.find('#modalTemperature').text(button.data('temperature') + ' ℃');
        modal.find('#modalCurrentPower').text(button.data('current-power') + ' Вт');
        
        var statusText = '';
        var statusClass = '';
        switch (button.data('status')) {
            case '1':
                statusText = 'Online';
                statusClass = 'text-success';
                break;
            case '0':
                statusText = 'Waiting';
                statusClass = 'text-secondary';
                break;
            case '3':
                statusText = 'Fault';
                statusClass = 'text-danger';
                break;
        }
        modal.find('#modalStatus').html('<span class="' + statusClass + '">' + statusText + '</span>');

        var tableBody = modal.find('#dataTable');
        tableBody.empty();

        // Populate the table if a matching entry is found
        if (filteredInfo) {

            filteredInfo.data_list.forEach(function (item, index) {
                var date = new Date(item.create_date);
                date.setHours(date.getHours() + 5);
                var formattedTime = date.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });

                var row = `<tr>
                            <td class="number-column">${index + 1}</td>
                            <td>${formattedTime}</td>
                            <td><strong>${item.data} Вт</strong></td>
                        </tr>`;
                tableBody.append(row);
            });
        } else {
            tableBody.append('<tr><td colspan="3">No data available</td></tr>');
        }

        // var modalLink = document.getElementById('modalLink');
        // modalLink.href = '/inverter/' + serial;
    });
});
