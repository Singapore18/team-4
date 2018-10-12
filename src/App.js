import React, { Component } from 'react';
import StudentDataComponent  from './StudentData'
import { Switch, Route } from 'react-router-dom'
import './App.css';
<<<<<<< HEAD
//import Login from './login'
import Chart from './chart'
=======
import Login from './login'
import QuestionComponent from './Question'
>>>>>>> 4a1db354ef5c28d9ccfa728a92bec75574360de0

class App extends Component {
  render() {
    return (
      <div className="App">
<<<<<<< HEAD
        {/* <Login/> */}
        <Chart/>
=======
      <Switch>
        <Route exact path='/' component={Login}/>
        <Route path='/survey' component={QuestionComponent}/>
      </Switch>
>>>>>>> 4a1db354ef5c28d9ccfa728a92bec75574360de0
      </div>
    );
  }
}

export default App;
