// Fetch and populate items table
$.getJSON('item/', function(data) {
    var itemsTableBody = $('#itemsTableBody');
    $.each(data, function(index, item) {
        var row = $('<tr></tr>');
        row.append('<td>' + item.name + '</td>');
        row.append('<td>' + item.value + ' $</td>');
        itemsTableBody.append(row);
    });
});
