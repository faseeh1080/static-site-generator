// Select all buttons with the class 'download-btn'
const buttons = document.querySelectorAll('.download-btn');

// Loop through each button and add a click event listener
buttons.forEach(button => {
  button.addEventListener('click', function() {
    button.textContent = 'Thanks';  // Change text to check mark
  });
});