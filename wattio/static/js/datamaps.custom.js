"use strict";

var mapUSA, mapUSABox = document.getElementById("dataMapUSA");
mapUSABox && (mapUSA = new Datamap({
    element: mapUSABox,
    scope: "usa",
    responsive: !0,
    aspectRatio: .45,
    data: {
        CA: {
            fillKey: "MEDIUM"
        },
        TX: {
            fillKey: "HIGH"
        },
        WA: {
            fillKey: "HIGH"
        },
        OK: {
            fillKey: "MEDIUM"
        },
        NC: {
            fillKey: "MEDIUM"
        },
        IN: {
            fillKey: "LOW"
        },
        IL: {
            fillKey: "LOW"
        },
        MT: {
            fillKey: "HIGH"
        }
    },
    fills: {
        HIGH: base.primaryColorLight,
        MEDIUM: base.primaryColor,
        LOW: base.primaryColorDark,
        defaultFill: colors.mutedColor
    },
    geographyConfig: {
        borderColor: colors.borderColor,
        highlightBorderWidth: 1
    }
}), window.addEventListener("resize", function() {
    mapUSA.resize()
}));