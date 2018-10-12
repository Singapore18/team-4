import React from 'react';
import './login.css'
import '../Question/styles.css'
import { Link } from 'react-router-dom'

export default class Login extends React.Component {
    render() {
        return (
            <div>
                <div style={{position:'fixed', left:"45%"}} className="logo-container">
                    <img src={require("./halogen-logo.png")}/>
                </div>

                <div className="login-container">
                    <form className="form-style" style={{padding: '100px', width:'15%'}} id="username" action="/">
                            <div style={{marginBottom:'15px', width:'100%', display:'flex', justifyContent:'space-between', alignItems:'center'}}>
                                <label style={{fontSize: '17px'}}>Username </label>
                                <input style={{width: '60%', height:'30px'}} type="text" name="uname"></input>
                            </div>
                            <div style={{width:'100%', display:'flex', justifyContent:'space-between', alignItems:'center'}}>
                                <label style={{fontSize: '17px'}}>Password </label>
                                <input style={{width: '60%', height:'30px'}} type="password" name="password"></input>
                            </div>
                            <button className="submit-button"><Link style={{textDecoration:'none', color:'white'}} to='/survey'>Login!</Link></button>
                        </form> 
                        
                </div>
            </div>
        )
    }
}
