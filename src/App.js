import React, { Component } from 'react';
import StudentDataComponent  from './StudentData'
import { Switch, Route } from 'react-router-dom'
import './App.css';
import Login from './login'
import QuestionComponent from './Question'
import ChartOverall from './chart (overall)'
import Chart from './chart (student)'

class App extends Component {
  render() {
    return (
      <div className="App">
      <Switch>
        <Route exact path='/' component={Login}/>
        <Route path='/survey' component={QuestionComponent}/>
        <Route path='/chartstudent' component={Chart}/>
        <Route path='/chartoverall' component={ChartOverall}/>
      </Switch>
      </div>
    );
  }
}

export default App;
