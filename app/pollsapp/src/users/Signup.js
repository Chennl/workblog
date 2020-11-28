import React from 'react';
import axios from 'axios';

class Signup extends React.Component{
    constructor(props){
        super(props);
        this.state = {showing:false,message:''}
    }
 
 

    handleInputChange=(e)=>{
        const target = e.target;
        const value = target.type ==='checkbox'?target.checked :target.value;
        const key = target.name;
        this.setState({[key]:value});
        console.log(key,'--',value);
    }

    handleSubmit = (e)=>{
        e.preventDefault();
        console.log(this.state);
        const {username,password,email} = this.state;
        axios.post('/api/users',{username,password,email},{
            headers: {
            'Content-Type': 'application/json',}
        })
        .then(response=>{
            var data = response.data;
            console.log(response);
            console.log(response.data);
            if(data.status ==='success'){
                this.setState({showing:true,message:data.message});

            }else{
                this.setState({showing:true,message:data.message});
            }
        })
        .catch(error=>{
            if(error.response.status === 400){
                this.setState({showing:true,message:error.response.data.message});
            }
            else{
                this.setState({showing:true,message:error.response.data.message});
            }
           // console.log("Error",error);
         })
         .then(function(){
             console.log('always executed');
         });
   

        // request.post('api/polls/signup',{username:username,password:password})
        // .then(res =>{
        //     console.log(res.data);
        //     if(res.data.status ==='fail'){
        //         this.setState({errmsg:res.data.errmsg,showing:true});
        //     }else{
        //         this.setState({errmsg:'',showing:false});
        //     }

        // })
        // .catch(err=>{
        //     this.setState({errmsg:'注册失败!',showing:true});
        //     console.log(err);
        // });

        e.preventDefault();
    }

    render(){
        const { showing,message } = this.state;
        return (
            <div className="container">
                <div className="row">
                    <form className="form-signin mx-auto" >
                        <h2 className="form-signin-heading" align="center">Sign up</h2>
                        <div className="form-group has-success">
                        <label htmlFor="username" className="sr-only">Username</label>
                        <input type="text" id="username" name="username" className="form-control" onChange={this.handleInputChange} placeholder="Username" required autoFocus />
                        </div>
                        <div className="form-group has-success">
                            <label htmlFor="email" className="sr-only">Email address</label>
                            <input type="email" id="email" name="email" className="form-control" onChange={this.handleInputChange} placeholder="Email address" required  />
                        </div>
                        <div className="form-group has-success">
                        <label htmlFor="password" className="sr-only">Password</label>
                        <input type="password" id="password" name="password" className="form-control" onChange={this.handleInputChange} placeholder="Password" required />
                        </div> 
                        <div className="form-check has-success">
                            <label htmlFor="password" className="form-check">
                                <input type="checkbox" id="agreement" name="agreement" className="form-check-input" onChange={this.handleInputChange}  required /><span className="text-info">同意并接受服务协议</span>
                            </label>
                        </div> 
                        <button className="btn btn-lg btn-success btn-block"  onClick={this.handleSubmit}>Sign up</button>
                        { showing ? <div> <p className="text-danger">{message}</p></div> : null }
                    </form>
                </div>
            </div>
        );
    }
}

export default Signup;