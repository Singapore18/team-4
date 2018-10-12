import React, { Component } from 'react';
import StudentDataComponent  from './StudentData'
import { Switch, Route } from 'react-router-dom'
import './App.css';
import Login from './login'
import QuestionComponent from './Question'

class App extends Component {
  render() {
    return (
      <div className="App">
      <Switch>
        <Route exact path='/' component={Login}/>
        <Route path='/survey' component={QuestionComponent}/>
      </Switch>
      </div>
    );
  }
}

export default App;
