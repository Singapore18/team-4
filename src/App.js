import React, { Component } from 'react';
import StudentDataComponent  from './StudentData'
import './App.css';
import Login from './login'

import QuestionComponent from './Question'

class App extends Component {
  render() {
    return (
      <div className="App">
        <StudentDataComponent />
      </div>
    );
  }
}

export default App;
