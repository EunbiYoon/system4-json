var chartData=JSON.parse('{{data|safe}}');
        var chartLabels=JSON.parse('{{ labels|safe }}');
        var chartConfig={
            type:'bar',
            data:{
                labels:chartLabels,
                datasets:[{
                    label:'Data',
                    data:chartData,
                    backgroundColor:'rgba(255,99,132,0.2)',
                    borderColor:'rgba(255,99,132,1)',
                    bordreWidth:1
                }]
            },
            options:{
                scales:{
                    y:{
                        beginAtZero:true
                    }
                }
            }
        };
        var chart=new Chart(document.getElementById('chart'), chartConfig);