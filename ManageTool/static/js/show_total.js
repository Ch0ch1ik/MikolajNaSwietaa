// pack into function show_total
$(document).ready(function () {
    function show_total() {
        let table = document.getElementById("sortMe");
        let sumVal = 0;
        document.getElementById("total").innerHTML = sumVal.toFixed(2);
        for (let i = 1; i < table.rows.length; i += 2) {
            sumVal = sumVal + parseFloat(table.rows[i].cells[18].innerText);
        }
        document.getElementById("total").innerText = sumVal.toFixed(2);
    }
    show_total();
});
