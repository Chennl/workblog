import React from 'react';

var TimeLeft = {
  color: '#999',
  fontSize: '15px'
}

class LivePreview extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            selected_option:'',
            disabled:0
        }
        this.voteHandler = this.voteHandler.bind(this);
        this.handleOptionChange = this.handleOptionChange.bind(this);
    }

    handleOptionChange(e){
        console.log(e.target.value);
        this.setState({selected_option: e.target.value });
    }
    
    voteHandler(e){
        e.preventDefault();
    
        var username = localStorage.getItem('username');
        //username = username ===null?'chennl':username;
        var data = {"poll_title": this.props.title, "option": this.state.selected_option,username};

        if( username ===null){
          alert('please to login before your voting!');
          return;
        }
        if(this.state.selected_option ===''){
          alert('please to select your option!');
          return;
        }
          
        //calls props handler
        this.props.voteHandler(data);
  
        //disable the button
        this.setState({disabled: 1});
    
    }
    render(){
        var options = this.props.options.map((option)=>{
            if(option.name){
                // calculate progress bar percentage
                var progress = Math.round((option.vote_count / this.props.total_vote_count) * 100) || 0;
                var current = {width: progress+"%"};
                return (
                    <div key={option.name}>
                      <input name="options" type="radio" value={option.name} onChange={this.handleOptionChange} /> {option.name}
                      <div className="progress">
                        <div className="progress-bar progress-bar-success" role="progressbar" aria-valuenow={progress}
                        aria-valuemin="0" aria-valuemax="100" style={current}>
                          {progress}%
                        </div>
                      </div>
                    </div>
                  );
            }else{
              return('')
            }
        });

        return(
            <div className={this.props.classContext}>
              <div className="card  mx-auto">
                <div className="card-header">
                  <h5>{this.props.title}</h5>
                </div>
                <div className="card-body">
                  <form onSubmit={this.voteHandler}>
                    {options}
                    <br />
                    <button type="submit" disabled={this.state.disabled}
                    className="btn btn-success btn-outline hvr-grow">Vote!</button>
                    <small> {this.props.total_vote_count} votes so far</small>
                    <small style={TimeLeft}> | {this.props.close_date}</small>
                  </form>
                </div>
              </div>
            </div>
          )
    }
}



export default LivePreview;