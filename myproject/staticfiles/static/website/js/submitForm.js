// Handle form submission
$('#itemForm').submit(function(event) {
    event.preventDefault();
    var itemId = $('#itemId').val();
    var itemName = $('#itemName').val();
    var itemValue = $('#itemValue').val();

    var requestData = {
        item_id: itemId,
        name: itemName,
        value: itemValue
    };

    $.ajax({
        url: 'http://localhost:8000/item/',
        method: 'PUT',
        data: JSON.stringify(requestData),
        dataType: 'json',
        contentType: 'application/json',
        success: function() {
        alert('Item updated successfully!');
        $('#itemForm')[0].reset();
        },
        error: function() {
        alert('Error updating item!');
        }
    });
});