const $last = $("#lastName");
const $first = $("#firstName");



$(window).on("load", function() {
    $("form").html("");

    setTimeout(function() {
        location.href = "/login";
    }, 10000);
});



