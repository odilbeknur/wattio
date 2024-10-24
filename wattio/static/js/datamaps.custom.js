var regionNameMapping = {
    "Kashkadarya": "Кашкадарья",
    "Tashkent": "Ташкент",
    "Samarkand": "Самарканд",
    "Bukhoro": "Бухара",
    "Khorezm": "Хорезм",
    "Navoi": "Наваи",
    "Ferghana": "Фергана",
    "Mubarek": "Мубарек",
    "Sirdaryo": "Сырдарья",
    "Angren": "Ангрен",
    "Turakurgan": "Туракурган",
    "Namangan": "Наманган",
    "Jizzakh": "Джизак",
    "Surkhandarya": "Сурхандарья",
    "Nukus": "Нукус",
    "Karakalpakstan": "Каракалпакстан",
    "Andijon": "Андижан",
    "Kashkadarya": "Кашкадарья",
    "Bukhara": "Бухара"
};

var mapUZB, mapUZBox = document.getElementById("container");
mapUZBox && (mapUZB = new Datamap({
    element: document.getElementById('container'),
    scope: 'uzb',
    responsive: !0,
    aspectRatio: .45,
    setProjection: function (element) {
        // Get the width and height of the container element
        var width = element.offsetWidth;
        var height = element.offsetHeight;

        var scale = Math.min(width, height)*4;

        var centerLongitude = 60; // Longitude of Uzbekistan
        var centerLatitude = 39; // Latitude of Uzbekistan
        var adaptiveLongitude = centerLongitude + (width - height) / width * 5; // Adjust for width
        var adaptiveLatitude = centerLatitude - (height - width) / height * 2; // Adjust for height

        // Define the projection with the adaptive center
        var projection = d3.geo.mercator()
            .center([adaptiveLongitude, adaptiveLatitude])  // Adaptive center
            .scale(scale)                                   // Dynamic scale based on element size
            .translate([width / 2, height / 2]);             // Center the map in the container

        var path = d3.geo.path().projection(projection);

        return { path: path, projection: projection };
    },

    fills: {
        defaultFill: "#ffff", // Цвет по умолчанию
        'UZB': '#0f75fa',    
        'Tashkent': '#0f75fa',
    },
    data: {
    Tashkent: {
        fillKey: 'TASHKENT'
    }
    },
    geographyConfig: {
        highlightOnHover: true,
        popupOnHover: true,
        borderColor: '#17a2b8',
        borderWidth: 1,
        highlightFillColor: '#17a2b8',
        highlightBorderColor: 'rgba(34,117,215,.25)',
        // Use the mapping in the popupTemplate
        popupTemplate: function (geo, data) {
            // Get the correct Russian name from the mapping
            const regionName = regionNameMapping[geo.properties.name] || geo.properties.name; // Default to original name if not found
            return '<div class="hoverinfo">' + regionName + '</div>';
        }
    }
}), window.addEventListener("resize", function () {
    mapUZB.resize()
}));


mapUZB.bubbles(oblasts.map(function (oblast) {
    return {
        name: oblast.name,
        latitude: oblast.latitude,
        longitude: oblast.longitude,
        radius: 8, // Радиус круга
        fillKey: 'UZB',
        url: '/plant/' + oblast.id,
        count: oblast.inverter_count,
        power: oblast.power
    };
}), {
    // Всплывающая подсказка при наведении (popover) с информацией о количестве инверторов и мощности
    popupTemplate: function (geo, data) {
        return '<div class="hoverinfo">' +
            '<strong>' + data.name + '</strong><br>' +
            'Мощность: ' + data.power + ' кВт <br>' +
            'Инверторы: ' + data.count + '<br>' +  // Corrected this line
            '</div>';
    }
});

// Сделать метки кликабельными
d3.selectAll('.datamaps-bubble').on('click', function (bubble) {
    window.location.href = bubble.url; // Перенаправление при нажатии на метку
});