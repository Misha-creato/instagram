
$(document).ready(function() {
  var searchInput = $("#search-input");

  searchInput.on("input", function() {
    var query = searchInput.val().trim();
    console.log(query)

    $.ajax({
      url: 'http://127.0.0.1:8000/profile/search/', 
      method: "GET",
      data: { query: query }, // Pass the search query as a parameter
      success: function(response) {
        let usersBox = $(".users-box")[0]
        console.log(usersBox)
        usersBox.innerHTML = ''
        response['profiles'].forEach(element => {
            let url = `http://127.0.0.1:8000/profile/${element.id}/`
            let userLink = document.createElement('a')
            userLink.className = 'user-link'
            userLink.href = url
            userLink.text = `${element.username}`
            
            usersBox.appendChild(userLink)
            let links = usersBox.querySelector('.user-link')
            console.log(links)

        });
      },
      error: function(xhr, status, error) {
        // Handle any errors that occur during the AJAX request
        console.error(error);
      }
    });
  });
});

