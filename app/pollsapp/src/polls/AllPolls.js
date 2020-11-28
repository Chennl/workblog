import React from 'react';
import LivePreviewProps from './LivePreviewProps';
import http from '../service/http';

// css style to align text to the center of it's container
var Align = {
  textAlign: 'center',
  fontFamily: 'EB Garamond'
};

 
//global variable to store origin url (e.g http://localhost:5000)
var origin = window.location.origin;


class AllPolls extends React.Component{

    constructor(props){
        super(props);
        this.state = {polls: {'Polls': []}, header: '', classContext: ''};
        console.log(props);

    }
  
    loadPollsFromServer=()=>{
      // pollName is available as a prop
      var pollName =  this.props.match.params.pollName;
      console.log(pollName);
      var url ='';
      if(pollName){
          url = '/api/polls/' + pollName
          this.setState({classContext: 'col-sm-6 col-sm-offset-3'})
  
      } else {
          url = '/api/polls'
          this.setState({header: 'Latest polls', classContext: 'col-sm-6'})
      }
      //make get request
      http.get(url)
      .then(response=>{
        this.setState({polls: response.data});
      })
      .catch(error=>{
        console.error(url, status, error.toString());
      });
    }
  
    componentDidMount(){
      this.loadPollsFromServer()
    }
  
    render(){
  
      // if a message was returned in the json result (the poll wasn't found)
      if(!this.state.polls.message){
      return (
        <LivePreviewProps polls={this.state.polls} loadPollsFromServer={this.loadPollsFromServer}
        header={this.state.header} classContext={this.state.classContext} />
        );
      } else {
        return (
            <div style={Align}>
              <h1>Poll not found</h1>
              <p>You might be interested in these <a href="/">polls</a></p>
            </div>
          )
        }
      }
    }


export default AllPolls;
  