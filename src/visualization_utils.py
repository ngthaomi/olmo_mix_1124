from IPython.display import display, HTML, Javascript

def render_bar_chart(data):
    html_setup = """
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <div><canvas id="barChart" width="600" height="300"></canvas></div>
    """
    display(HTML(html_setup))
    js_data = f"""
    var barChartData = {{
        labels: {data['labels']},
        datasets: [
            {{label: 'Positive', data: {data['positive']}, backgroundColor: 'rgba(75, 192, 192, 0.6)'}},
            {{label: 'Neutral', data: {data['neutral']}, backgroundColor: 'rgba(153, 162, 235, 0.6)'}},
            {{label: 'Negative', data: {data['negative']}, backgroundColor: 'rgba(255, 99, 132, 0.6)'}}
        ]
    }};"""
    js_render = """
    new Chart(document.getElementById('barChart').getContext('2d'), {
        type: 'bar', data: barChartData, options: {scales: {y: {beginAtZero: true}}}
    });"""
    display(Javascript(js_data + js_render))

def render_line_chart(data):
    html_setup = """
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <div><canvas id="lineChart" width="600" height="300"></canvas></div>
    """
    display(HTML(html_setup))
    js_data = f"""
    var lineChartData = {{
        labels: {data['time_labels']},
        datasets: [
            {{label: 'Lloyds', data: {data['lloyds_data']}, borderColor: 'rgba(75, 192, 192, 1)'}},
            {{label: 'Barclays', data: {data['barclays_data']}, borderColor: 'rgba(255, 99, 132, 1)'}}
        ]
    }};"""
    js_render = """
    new Chart(document.getElementById('lineChart').getContext('2d'), {
        type: 'line', data: lineChartData, options: {scales: {y: {beginAtZero: true}}}
    });"""
    display(Javascript(js_data + js_render))