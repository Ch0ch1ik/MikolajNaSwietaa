function show_id(event) {



    var ids = get_checked_chexboxes();
    var params = new URLSearchParams();
    // var score = document.getElementById("score_over").value;

    var region = get_region();
    var type = get_type();
    var santa = get_santa();

    params.append("region", region);
    params.append("type", type);
    params.append("bounded_santa", santa);

    // params.append("score", score);
    ids.forEach(id => params.append("filter_by", id))
    var address = '/show_filtered_orders/?' + params.toString();

    fetch(address)
        .then(response => response.text())
        .then(data => document.getElementById("orders").innerHTML = data);

}

function get_type() {
    var position = document.getElementById("typ_wizyty");
    return position.value;
}
function get_santa() {
    var santa = document.getElementById("bounded_santa");
    return santa.value;
}

function get_region() {
    var region = document.getElementsByClassName("nav-link active")[0];
    return region.textContent;
}

function get_checked_chexboxes() {
    var markedCheckbox = document.querySelectorAll('input[type="checkbox"]:checked');
    var ids = [];
    markedCheckbox.forEach(box => ids.push(box.value));
    return ids;
}


$(document).ready(function () {
    var li_buttons = $('.checkboxy');
    var nav_items = $('.nav-tabs li.nav-item');
    nav_items.click(show_id);
    li_buttons.click(show_id);
});

