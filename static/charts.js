fetch('/get-chart-data')
    .then(response => response.json())
    .then(data => {
        const ctx = document.getElementById('expenseChart').getContext('2d');
        
        // Create a new pie chart with dynamic data
        new Chart(ctx, {
            type: 'pie', // Use 'pie' chart type
            data: {
                labels: data.categories, // The categories from the API
                datasets: [{
                    data: data.amounts, // The amounts for each category
                    backgroundColor: ['#ff6384', '#36a2eb', '#ffcd56', '#4bc0c0', '#9966ff'], // Pie chart colors
                    hoverOffset: 4 // Offset for hover effect
                }]
            },
            options: {
                responsive: true, // Ensures the chart is responsive
                maintainAspectRatio: false, // Allows the chart to resize properly on different devices
                plugins: {
                    legend: {
                        position: 'top', // Place the legend at the top
                    }
                }
            }
        });
    });
