function show_id(event) {
        var ids = get_checked_chexboxes();
        var params = new URLSearchParams();


        var score = document.getElementById("score_over").value;

        params.append("score", score);


        ids.forEach(id => params.append("filter_by", id))
        var address = '/show_filtered_applications?' + params.toString();
        fetch(address)
            .then(response => response.text())
            .then(data => document.getElementById("applications").innerHTML = data);

    }

    function get_checked_chexboxes() {
        var markedCheckbox = document.querySelectorAll('input[type="checkbox"]:checked');
        var ids = [];
        markedCheckbox.forEach(box => ids.push(box.value));
        console.log(ids);
        return ids;
    }


    $(document).ready(function () {
        var li_buttons = $('.checkboxy');
        li_buttons.click(show_id);
    });

    // function filter_by_score() {
    //     var score = document.getElementById("score_over").value;
    //     console.log(score);
    //     var params = new URLSearchParams();
    //     params.append("score", score);
    //     var address = '/show_filtered_applications?' + params.toString();
    //     fetch(address)
    //         .then(response => response.text())
    //         .then(data => document.getElementById("applications").innerHTML = data);
    // }