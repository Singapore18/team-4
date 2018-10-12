import React from 'react';
//import './login.css'
import {Bar} from 'react-chartjs-2';

/*const data= {
    labels: ["January", "February", "March", "April", "May", "June", "July"],
    datasets: [{
        label: "My First dataset",
        backgroundColor: 'rgb(255, 99, 132)',
        borderColor: 'rgb(255, 99, 132)',
        data: [0, 10, 5, 2, 20, 30, 45],
    }]
}*/

const data = {
    labels: ["Mindset", "Resilience", "Self-Esteem", "Self-Efficacy", "Curiousity", "Visioning", 
        "Inquiry & Exploration", "Active Empathic Listening", "Collaboration", "Delayed Gratification", "Productivity"],
    datasets: [
        {
            label: "Score",
            data: [6.5, 5.5, 7, 6, 5, 4, 5.5, 6, 4, 4, 5],
            backgroundColor: ["#3e95cd", "#3e95cd", "#8e5ea2", "#8e5ea2", "#8e5ea2", "#3cba9f", "#3cba9f", "#3cba9f",
                "#e8c3b9", "#e8c3b9", "#c45850", "#c45850"]
        }
    ],
    options: {
        legend: { display: false },
        title: {
          display: true,
          text: 'xx Score'
        },
        scales: {
            yAxes: [{
                ticks: {
                    suggestedMin:0
                }
            }]
        }
    }
}

const options = {
    
}

export default class Chart extends React.Component {
    /*componentDidMount() {
        console.log(this.refs.chart.chartInstance); // returns a Chart.js instance reference
    }*/

    render() {
        return (
            <Bar
                data={data}
                options={{
                    legend: { display: false },
                    title: {
                      display: true,
                      text: 'xx Score'
                    },
                    scales: {
                        yAxes: [{
                            ticks: {
                                suggestedMin:0
                            }
                        }]
                    }
                }}
            />  
            //<Bar ref='chart'  data={data} />
            //<div>test</div>

        )
    }
}
