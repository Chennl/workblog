import React from 'react';
import {Link} from 'react-router-dom';

const activeStyle = {  fontWeight: "bold"   }

class Home extends React.Component{
    constructor(props){
        super(props);
        this.state={}
    }
    render(){
        var username = localStorage.getItem('username');
        if(username){
            
            return(
                <div className="container">

                    <div className="col-lg-6">
                        <h3>Hi {username}, welcome to be back!  </h3>
                        <p>Please click the link below to start your polling journey.</p>
                        <Link className="nav-link"  to="/polls">Polls</Link>
                    </div>
                </div>
           
            );
        }else{
            return (
                <div className="container">
                    <div className="col-lg-6">
                        <h3>It's so easy</h3>
                        <p>It's so easy to use Votr, just create an account and you can start creating polls for the world to see!</p>
                    </div>
                    <div className="col-lg-6">
                        <Link className="nav-link" activeStyle={activeStyle} to="/login">Login</Link>
                    </div>
                </div>
            );
        }
    }

}

export default Home;