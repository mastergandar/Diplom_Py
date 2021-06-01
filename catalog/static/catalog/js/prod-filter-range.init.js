$(document).ready(function () {
    $("#priceranger").ionRangeSlider({
        skin: "flat",
        type: "double",
        grid: !0,
        min: 0,
        max: 1e5,
        from: 200,
        to: 800,
        prefix: "₽"
    })
});