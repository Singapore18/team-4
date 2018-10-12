import React from 'react';
import './login.css'

export default class Login extends React.Component {
    render() {
        return (
            <div>
                <div style={{position:'fixed', left:"45%"}} className="logo-container">
                    <img src={require("./halogen-logo.png")}/>
                </div>

                <div className="login-container">
                <form id="username" action="/">
                        <label>Username </label>
                        <input type="text" name="uname"></input>
                        <br></br>
                        <label>Password </label>
                        <input type = "password" name="pass"></input>
                        <br></br>
                        <br></br>
                        <input type="button" onclick="myFunction()" value="Submit"></input>
                    </form>
                </div>
            </div>
        )
    }
}
