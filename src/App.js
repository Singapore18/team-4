import React, { Component } from 'react';
import StudentDataComponent  from './StudentData'
import { Switch, Route } from 'react-router-dom'
import './App.css';
import Login from './login'
import QuestionComponent from './Question'
import QuizComponent from './Quiz'
import QuestionaireComponent from './Questionaire' 
import Thank from './Thank'

class App extends Component {
  render() {
    return (
      <div className="App">
      <Switch>
        <Route exact path='/' component={Login}/>
        <Route path='/survey' component={QuestionComponent}/>
        <Route path='/quiz' component={QuizComponent}/>
        <Route path='/questionaire' component={QuestionaireComponent}/>
        <Route path='/keystonequiz' component={QuestionComponent}/>
        <Route path='/thankyou' component={Thank} />
      </Switch>
      </div>
    );
  }
}

export default App;
