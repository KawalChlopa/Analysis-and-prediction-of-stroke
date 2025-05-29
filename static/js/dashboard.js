async function fetchAndRender(endpoint, canvasId, labelField, valueField, chartType = 'bar') {
    const response = await fetch(endpoint);
    const data = await response.json();

    const labels = data.map(item => item[labelField]);
    const values = data.map(item => item[valueField]);

    new Chart(document.getElementById(canvasId).getContext('2d'), {
        type: chartType,
        data: {
            labels: labels,
            datasets: [{
                label: canvasId.replace('Chart', ''),
                data: values,
                backgroundColor: 'rgba(75, 192, 192, 0.6)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: true }
            }
        }
    });
}

window.onload = () => {
    fetchAndRender('/api/Age', 'ageChart', 'AgeGroup', 'Probability');
    fetchAndRender('/api/Sex', 'sexChart', 'Sex', 'Probability');
    fetchAndRender('/api/RaceEthnicity', 'raceChart', 'Race', 'Probability');
    fetchAndRender('/api/Smokers', 'smokersChart', 'SmokingStatus', 'Probability');
    fetchAndRender('/api/GeneralHealth', 'healthChart', 'HealthStatus', 'Probability');
    fetchAndRender('/api/Asthma', 'asthmaChart', 'Asthma', 'Probability');
    fetchAndRender('/api/Stroke', 'strokeChart', 'Stroke', 'Probability');
};
