$(document).ready(function() {
    // Load the initial content
    loadContent('homePage');
  
    // Handle navbar item click event
    $('.nav-link').click(function(e) {
      e.preventDefault(); // Prevent the default behavior of the anchor tag
  
      var page = $(this).attr('href'); // Get the page from the href attribute
      page = page.substring(1); // Remove the leading slash
  
      loadContent(page); // Load the content for the clicked page
    });
  });
  
  function loadContent(page) {
    $.ajax({
      url: page,
      method: 'GET',
      success: function(data) {
        $('#content').html(data);
      },
      error: function() {
        $('#content').html('<h1>Page not found!</h1>');
      }
    });
}