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
    "Bukhara": "Бухара"
};

var mapUZB, mapUZBox = document.getElementById("container");
mapUZBox && (mapUZB = new Datamap({
    element: document.getElementById('container'),
    scope: 'uzb',
    responsive: true,
    aspectRatio: .45,
    setProjection: function (element) {
        var width = element.offsetWidth;
        var height = element.offsetHeight;

        var scale = Math.min(width, height) * 5;

        var centerLongitude = 60;
        var centerLatitude = 39;
        var adaptiveLongitude = centerLongitude + (width - height) / width * 5;
        var adaptiveLatitude = centerLatitude - (height - width) / height * 2;

        var projection = d3.geo.mercator()
            .center([adaptiveLongitude, adaptiveLatitude])
            .scale(scale)
            .translate([width / 2, height / 2]);

        var path = d3.geo.path().projection(projection);

        return { path: path, projection: projection };
    },

    fills: {
        defaultFill: "#f4f4f4",  // default region color
        'UZB': '#0f75fa',        // Uzbekistan's color
        'Tashkent': '#FF5733',    // Tashkent color
        'Samarkand': '#33FF57',   // Samarkand color
        'Bukhoro': '#3357FF',     // Bukhoro color
    },
    data: {
        Tashkent: { fillKey: 'Tashkent' },
        Samarkand: { fillKey: 'Samarkand' },
        Bukhoro: { fillKey: 'Bukhoro' },
        // Add more regions with their fillKey as needed
    },
    geographyConfig: {
        highlightOnHover: true,
        popupOnHover: true,
        borderColor: '#17a2b8',
        borderWidth: 1,
        highlightFillColor: '#17a2b8',
        highlightBorderColor: 'rgba(34,117,215,.25)',
        popupTemplate: function (geo, data) {
            const regionName = regionNameMapping[geo.properties.name] || geo.properties.name;
            return '<div class="hoverinfo">' + regionName + '</div>';
        }
    }
}), window.addEventListener("resize", function () {
    mapUZB.resize();
}));

mapUZB.bubbles(oblasts.map(function (oblast) {
    return {
        name: oblast.name,
        latitude: oblast.latitude,
        longitude: oblast.longitude,
        radius: 8,
        fillKey: 'UZB',
        url: '/plant/' + oblast.id,
        count: oblast.inverter_count,
        power: oblast.power
    };
}), {
    popupTemplate: function (geo, data) {
        return '<div class="hoverinfo">' +
            '<strong>' + data.name + '</strong><br>' +
            'Мощность: ' + data.power + ' кВт <br>' +
            'Инверторы: ' + data.count + '<br>' +
            '</div>';
    }
});

d3.selectAll('.datamaps-bubble').on('click', function (bubble) {
    window.location.href = bubble.url;
});
