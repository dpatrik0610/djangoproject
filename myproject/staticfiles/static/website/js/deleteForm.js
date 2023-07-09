$(document).ready(function() {
    // Delete button click event
    $('#deleteButton').click(function() {
      var itemId = $('#itemId').val(); // Get the item ID from the input field
  
      $.ajax({
        url: '/item/?id=' + itemId, // Pass the item ID as a parameter in the URL
        type: 'DELETE',
        success: function(response) {
            alert("Item " + itemId + " deleted successfully!");
            console.log(response);
        },
        error: function(error) {
            alert("Deleting item Failed!\nCheck Console!")
            console.log(error);
        }
      });
    });
  });