import React from 'react'
import './styles.css'
import { qn, sevenPoint } from './constants'



export default class QuestionComponent extends React.Component {

    constructor(props){
        super(props)
        this.handleChange = this.handleChange.bind(this)
        this.state = {
            name: 'darryl'
        }
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
                <div style={{padding:'20px', backgroundColor:'white', width: '40%'}}>
                    <p>
                        Questionarie
                    </p>
                    <form>
                    {
                        qn.map((item, index) => {
                            return (
                                <div key={index} className="question-wrapper">
                                    <label>
                                        {index+1}) {item.question}
                                    </label>
                                    <select 
                                        onChange={(event) => this.handleChange(event, index)}
                                        required>
                                        <option disabled selected> </option>
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