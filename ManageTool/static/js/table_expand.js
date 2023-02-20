$(document).ready(function () {

        //
        $('.btn-table-expand').on('click', function () {
            let $tr = $(this).closest('tr');

            if ($(this).data('expanded') === undefined || $(this).data('expanded') === 'false') {
                $(this).data('expanded', 'true')
                $(this).children('i').attr('class', 'fa fa-minus');
                $('#' + $tr.data('target')).show();
            } else {
                $(this).data('expanded', 'false')
                $(this).children('i').attr('class', 'fa fa-plus');
                $('#' + $tr.data('target')).hide();
            }
        });
    });