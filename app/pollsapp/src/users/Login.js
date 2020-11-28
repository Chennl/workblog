import React from 'react';
import axios from 'axios';
import qs from 'qs';
import {Link,Redirect } from 'react-router-dom';
import http from '../service/http';
 
import { message, Button, Space } from 'antd';

 

const error = (msg) => {
  // alert(msg);
 //antd
  message.error(msg,3);
};

class Login extends React.Component{
    constructor(props){
        super(props);
        const {location,match,history} = this.props; 
        this.state = { username:'',location,match,history};
        console.log(this.state);
    }
    showSuccess = (msg) => {
      // alert(msg);
      //antd
      message.success(msg,3);
    }
    showError = (msg) => {
      // alert(msg);
     //antd
      message.error(msg,3);
    };
    handleInputChange=(e)=>{
      const target = e.target;
      const value = target.type ==='checkbox'?target.checked :target.value;
      const key = target.name;
      this.setState({[key]:value});
    } 

    handleLogin=(e)=>{
      console.log(this.state)
      const {username,password} = this.state;
      
      //qs.stringify 'name=hehe&age=10'  JSON.stringnify '{"name":"hehe","age":10}'
      http.post('/api/users/login',{username,password}) 
      .then(res =>{
          //console.log(res.data);
          var token = res.data.token;
          localStorage.setItem('token',token);
          localStorage.setItem('username',username);
          this.setState({token});
          
          this.showSuccess(res.data.message);
          this.state.history.push('/polls');

      })
      .catch( error =>{
          var msg='';
          if(error.response.data.message)
            msg =error.response.data.message;
          else if(error.response.data.error){
            msg =error.response.data.error;
          }
          else
            msg=error.response.StatusText;

          console.error(error);
          alert(msg);
      });
    }

    handleClick=(e)=>{
      //useHistory
      //this.state.history.push('/search');

    }
    render(){
      //const {history} = this.props;
      if(this.state.isAuthenticated){
        console.log('Redirecting..')
        return <Redirect  to="/home" />
      }
      else
        return (
            <div className="container">
              <div className="row">
                <div className="col-lg-6">
                  <h3>It's so easy</h3>
                  <p>It's so easy to use Votr, just create an account and you can start
                  creating polls for the world to see!</p>
                  <button type="button" onClick={this.handleClick}>
                    Go home test
                  </button>
                </div>
  
                <div className="col-lg-6">
                  <h3 className="form-header">Login</h3>

                  <div >
                    <div className="form-group has-success">
                      <input type="text" className="form-control" onChange={this.handleInputChange} name="username" placeholder="Username" />
                    </div>
  
                    <div className="form-group has-success">
                      <input type="password" className="form-control"onChange={this.handleInputChange}  name="password" placeholder="Password" />
                    </div>
  
                    <button className="btn btn-success" onClick={this.handleLogin} >Login</button>

                    <Link to={{
                            pathname: "/signup",
                            search: "?sort=name",
                            hash: "#the-hash",
                            state: {isAuthorized: true,...this.state }
                          }}
                        >singup</Link>
                  </div>
                </div> 
              </div>
        </div>
  
        )
    }
}

export default Login; 