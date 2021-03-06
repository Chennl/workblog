import React from 'react';
import LivePreview from './LivePreview';
import http from '../service/http'

// css style to align text to the center of it's container
var Align = {
  textAlign: 'center',
  fontFamily: 'EB Garamond'
};

var TimeLeft = {
  color: '#999',
  fontSize: '15px'
}

//global variable to store origin url (e.g http://localhost:5000)
var origin = window.location.origin;


class LivePreviewProps extends React.Component{
    constructor(props){
        super(props);
        this.state={}
    }

    voteHandler(data){
      var url =  origin + '/api/poll/vote'
      //console.log(data);
      // make patch request
      http({url,data,method:'PATCH'})
      .then(response =>{
        alert(response.data.message)
      })
      .catch(error=>{
        if (error.response) {
          // The request was made and the server responded with a status code
          // that falls out of the range of 2xx
          alert(error.response.data.message);
          console.log(error.response);

        } else if (error.request) {
          // The request was made but no response was received
          // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
          // http.ClientRequest in node.js
          console.log(error.request);
          alert(error.request)
        } else {
          // Something happened in setting up the request that triggered an Error
          console.log('Error', error.message);
        }
        console.log(error.config);
 
      });
      // $.ajax({
      //   url: url,
      //   dataType: 'json',
      //   type: 'PATCH',
      //   data: JSON.stringify(data),
      //   contentType: 'application/json; charset=utf-8',
      //   success: function(data){
      //     alert(data.message);
      //     this.setState({selected_option: ''});
      //     this.props.loadPollsFromServer();
      //   },
      //   error: function(xhr, status, err){
      //     alert('Poll creation failed: ' + err.toString());
      //   }
      // });
  
    }
  
    render(){
      var polls = this.props.polls.Polls.map(function(poll){
        var minutes = Math.floor((Date.parse(poll.close_date) - Date.now()) / (60000));
        var time_remaining = '';
  
        if(minutes > 1 && minutes < 59){
          time_remaining += minutes + ' minutes remaining';
        }
  
        else if(minutes < 1380){
          var hours =  Math.floor(minutes / 60);
          time_remaining += hours + ' hours remaining';
        }
  
        else {
          var days = Math.floor(minutes / (24 * 60));
          time_remaining += days + ' days remaining';
        }
  
        return (
          <LivePreview key={poll.title} title={poll.title} options={poll.options}
          total_vote_count={poll.total_vote_count} voteHandler={this.voteHandler}
          close_date={time_remaining} classContext={this.props.classContext} />
      );
    }.bind(this));
  
        return (
        <div>
            <h1 style={Align}>{this.props.header}</h1>
            <br />
            <div className="row">{polls}</div>
        </div>
        );
    }

  }

  export default LivePreviewProps;