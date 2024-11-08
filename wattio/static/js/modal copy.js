document.addEventListener('DOMContentLoaded', function () {
    $('.modal-shortcut').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget); // Button that triggered the modal
        var serial = button.data('serial');
        var plantLocation = document.getElementById('plant-data').getAttribute('data-location');
        console.log(plantLocation)

        if (plantLocation === 'JSC_TPP') {
            apiBaseUrl = "http://10.20.6.30:8080";  // TPP API URL
        } else if (plantLocation === 'TASHKENT_TTC') {
            apiBaseUrl = "http://10.20.96.35:8080";  // PTT API URL
        }
        else if (plantLocation === 'SIRDARYA_TPP') {
            apiBaseUrl = "http://10.28.28.50:8080";  // PTT API URL
        } else if (plantLocation === 'MUBAREK_TPP') {
            apiBaseUrl = "http://10.20.77.30:8080";  // PTT API URL
        }else {
            apiBaseUrl = "http://10.20.6.30:8080";  // Default API URL
        }
        
        // Construct the URL dynamically
        var baseUrl = `${apiBaseUrl}/data/chart/day/{serial_number}/yyyy-mm-dd`; 
        console.log(baseUrl)
        var todayDate = new Date().toISOString().split('T')[0]; // Get today's date in yyyy-mm-dd format
        var detailUrl = baseUrl.replace('{serial_number}', serial).replace('yyyy-mm-dd', todayDate); // Replace placeholders with actual values
        // Fetch data from the API
        fetch(detailUrl)
            .then(response => response.json())
            .then(data => {
                // Update the modal's content
                var modal = $(this);
                modal.find('#modalName').text(button.data('name'));
                modal.find('#modalModel').text(button.data('model'));
                modal.find('#modalSerial').text(serial);
                modal.find('#modalTotalEnergy').text(button.data('total-energy') + ' кВт·ч');
                modal.find('#modalTodayEnergy').text(button.data('today-generate-energy') + ' кВт·ч');
                modal.find('#modalTemperature').text(button.data('temperature') + ' ℃');
                modal.find('#modalCurrentPower').text(button.data('current-power') + ' Вт');
                modal.find('#modalTotalEnergy').text(button.data('total-energy') + ' кВт·ч');

                // Set status text based on status value
                var statusText = '';
                var statusClass = '';
                if (button.data('status') == '1') {
                    statusText = 'Online';
                    statusClass = 'text-success';
                } else if (button.data('status') == '0') {
                    statusText = 'Waiting';
                    statusClass = 'text-secondary';
                } else if (button.data('status') == '3') {
                    statusText = 'Fault';
                    statusClass = 'text-danger';
                }
                modal.find('#modalStatus').html('<span class="' + statusClass + '">' + statusText + '</span>');

                // Update the table with fetched data
                var tableBody = modal.find('#dataTable');
                tableBody.empty(); // Clear existing rows

                data.data_list.forEach(function (item, index) {
                    // Create a Date object from the item.create_date
                    var date = new Date(item.create_date);
                
                    // Add 5 hours to the date object
                    date.setHours(date.getHours() + 5);
                
                    // Format the date to HH:MM
                    var formattedTime = date.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });
                
                    // Create a row for the table
                    var row = `<tr>
                        <td class="number-column">${index + 1}</td>
                        <td>${formattedTime}</td>
                        <td><strong>${item.data} Вт</strong></td>
                    </tr>`;
                
                    // Append the row to the table body
                    tableBody.append(row);
                });
                
            })
            .catch(error => console.error('Error fetching data:', error));

        // Update the modal link
        var modalLink = document.getElementById('modalLink');
        modalLink.href = '/inverter/' + serial;
    });
});
