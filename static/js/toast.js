console.log('toast js loaded')

// Function to hide the toast message
function hideToast() {
    $("#toast").addClass('invisible');
}

// Calling the hide function when the button with the id
// of 'toast-button' is clicked
$("#toast-button").click(function(){
    hideToast()
    })
