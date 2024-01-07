document.addEventListener('DOMContentLoaded', function () {
    // Add an event listener to every button with the class 'convert-button'
    document.querySelectorAll('.convert-button').forEach(function(button) {
        button.addEventListener('click', function() {
            const blockId = button.getAttribute('data-block-id');

            // Make an AJAX call to your Django view
            fetch('http://127.0.0.1:8000/admin/convert_blocks/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken') // You need to include a function to get the CSRF token from cookies
                },
                body: JSON.stringify({
                    block_id: blockId,
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Block converted successfully!');
                } else {
                    alert('Conversion failed!');
                }
            });
        });
    });
});

// Function to get a cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
