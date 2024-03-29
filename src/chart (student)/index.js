import React from 'react';
import {Bar} from 'react-chartjs-2';

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
    ]
}


export default class Chart extends React.Component {

    render() {
        return (
            <Bar
                data={data}
                options={{
                    legend: { display: false },
                    title: {
                        display: true,
                        text: 'Your Score'
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

        )
    }
}
