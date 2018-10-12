import React from 'react'
import './styles.css'
import { qn, sevenPoint } from './constants'



export default class QuestionComponent extends React.Component {

    constructor(props){
        super(props)
        this.handleChange = this.handleChange.bind(this)
        this.state = {
            name: 'darryl',
            questions: []
        }
    }

    componentDidMount() {
        const that = this;
        fetch("http://localhost:5002/questions")
            .then(function(response) {                
                return response.json();
            })
            .then(function(data) {
                console.log(data)
                that.setState({ questions: data.json_list });
        });
    }

    handleChange(event, index){
        var val = event.target.value;
        if(questionArr[index] === null){
            questionArr.push(
                {
                    'id': index,
                    'answer': val
                }
            )
        }
        else {
            var temp = {
                'id': index,
                'answer': val
            }
            questionArr[index] = temp
        }
    }

    render(){
        return (
            <div className="question-container">
                <div style={{padding:'20px', backgroundColor:'white', width: '50%'}}>
                    <p>
                        Questionarie
                    </p>
                    <form>
                    {

                        this.state.questions.map((item, index) => {
                            return (
                                <div key={index} className="question-wrapper">
                                    <label>
                                        {index+1}) {item.question}
                                    </label>
                                    <select 
                                        onChange={(event) => this.handleChange(event, index)}
                                        required>
                                        {/* <option disabled selected> </option> */}
                                        {
                                            sevenPoint.map((item2, index2) => {
                                                return (
                                                    <option key={index2} value={index2+1}>
                                                        {item2}
                                                    </option>
                                                )
                                            })
                                        }
                                    </select>
                                </div>  
                            )
                        })
                    }
                        <button className="submit-button" type="submit">Submit</button>
                    </form>
                    {/* <button onClick={() => console.log(questionArr)}>Submit</button> */}
                </div>
            </div>
        )
    }
}

const questionArr = []