document.addEventListener('DOMContentLoaded', function () {

    const table = document.getElementById('sortMe');

    const headers = table.querySelectorAll('th.first');
    const tableBody = table.querySelector('tbody.first');
    const rows = tableBody.querySelectorAll('tr.first');

    // Track sort directions
    const directions = Array.from(headers).map(function (header) {
        return '';
    });

    // Transform the content of given cell in given column
    const transform = function (index, content) {
        // Get the data type of column
        const type = headers[index].getAttribute('data-type');
        switch (type) {
            case 'number':
                return parseFloat(content);
            case 'string':
            default:
                return content;
        }
    };

    const sortColumn = function (index) {
        // Get the current direction
        const direction = directions[index] || 'asc';

        // A factor based on the direction
        const multiplier = direction === 'asc' ? 1 : -1;

        const newRows = Array.from(rows);

        newRows.sort(function (rowA, rowB) {
            const cellA = rowA.querySelectorAll('td.first')[index].innerHTML;

            const cellB = rowB.querySelectorAll('td.first')[index].innerHTML;


            const a = transform(index, cellA);
            const b = transform(index, cellB);

            switch (true) {
                case a > b:
                    return 1 * multiplier;
                case a < b:
                    return -1 * multiplier;
                case a === b:
                    return 0;
            }
        });

        // Remove old rows
        [].forEach.call(rows, function (row) {
            tableBody.removeChild(row);
        });

        // Reverse the direction
        directions[index] = direction === 'asc' ? 'desc' : 'asc';

        // Append new row
        newRows.forEach(function (newRow) {
            tableBody.appendChild(newRow);
        });
    };

    [].forEach.call(headers, function (header, index) {
        header.addEventListener('click', function () {
            sortColumn(index);
        });
    });


});