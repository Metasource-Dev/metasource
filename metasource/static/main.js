// Script to handle content switching based on navbar links
document.getElementById('dashboard-link').addEventListener('click', function() {
    document.getElementById('dashboard-content').style.display = 'block';
    document.getElementById('quotations-content').style.display = 'none';
});

document.getElementById('quotations-link').addEventListener('click', function() {
    document.getElementById('dashboard-content').style.display = 'none';
    document.getElementById('quotations-content').style.display = 'block';
});

// Script to handle light/dark mode toggle
document.getElementById('toggle-mode').addEventListener('click', function() {
    // Replace with your logic to toggle between light and dark mode
    // You can update CSS classes or apply styles directly using JavaScript
    alert('Toggle between light and dark mode!');
});