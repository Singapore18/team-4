import React, { Component } from 'react';
import StudentDataComponent  from './StudentData'
import { Switch, Route } from 'react-router-dom'
import './App.css';

//import Login from './login'
// import Chart from './chart'

import Login from './login'
import QuestionComponent from './Question'

import QuizComponent from './Quiz'
import QuestionaireComponent from './Questionaire' 
import Thank from './Thank'

import Chart from './chart (student)'
import ChartOverall from './chart (overall)'



class App extends Component {
  render() {
    return (
      <div className="App">
      <Switch>
        <Route exact path='/' component={Login}/>
        <Route path='/survey' component={QuestionComponent}/>
        <Route path='/chartstudent' component={Chart}/>
        <Route path='/chartoverall' component={ChartOverall}/>
        <Route path='/quiz' component={QuizComponent}/>
        <Route path='/questionaire' component={QuestionaireComponent}/>
        <Route path='/keystonequiz' component={QuestionComponent}/>
        <Route path='/thankyou' component={Thank} />
        <Route path='/chart' component={Chart}/>
      </Switch>
      </div>
    );
  }
}

export default App;
