import React from 'react';
import http from '../service/http';
import LivePreview from './LivePreview';

// css style to align text to the center of it's container
var Align = {
  textAlign: 'center',
  fontFamily: 'EB Garamond'
};

 
//global variable to store origin url (e.g http://localhost:5000)
var origin = window.location.origin;

 
  
class PollForm extends React.Component {
    constructor(props){
        super(props);
        //close poll in 24 hours
        var close_date = new Date();
        close_date.setHours(close_date.getHours() + 24);
        close_date = close_date.getTime()/1000;
        this.state = {
            title: '', 
            option: '', 
            options: [], 
            close_date: close_date, 
            all_options: []
        };

        this.handleTitleChange = this.handleTitleChange.bind(this);
        this.handleOptionChange = this.handleOptionChange.bind(this);
        this.handleOptionAdd = this.handleOptionAdd.bind(this);
        this.onDateChange = this.onDateChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);

    }
    componentDidMount(){
        var url = origin +"/api/polls/options";
        
        http.get(url)
        .then(response=>{
            this.setState({all_options: [...response.data]});
            //console.log(response);
        })
        .catch(error=>{
            console.error(url,error);
        });
       
}

handleOptionAdd(){
    console.log('handleOptionAdd');
    //update poll options and reset options to an empty string
    //var duplicate = this.state.options.indexOf(this.state.option);
    var duplicate =  this.state.options.find(item=>item.name===this.state.option)
    if(duplicate)
        alert('duplicate options');
    else
        this.setState({
            options: this.state.options.concat({name: this.state.option}),
            option: ''
        });
}
handleOptionChange(e){
   // console.log('handleOptionChange',e)
    var option =e.target.value
    this.setState({option});
}
handleTitleChange(e){
    //change title as the user types
    var title = e.target.value;
    this.setState({title: title});
}
onDateChange(date){
    // convert date to UTC timestamp in seconds
    var close_date = date.getTime() / 1000
    //antd.message.info(`您选择的日期是: ${date ? date.format('YYYY-MM-DD') : '未选择'}`);
    this.setState({close_date: close_date})
    }
handleSubmit(e){
    e.preventDefault();
    var title = this.state.title;
    var options = this.state.options;
    var close_date = this.state.close_date;

    var data = {title: title,
                options: options.map(function(x){return x.name}),
                close_date: close_date
            };

    var url =  origin + '/api/polls'
    http.post(url,data)
    .then(response=>{
        alert(response.data.message);
    })
    .catch(error=>{
        console.error(error);
        alert('Fail to create poll');
    });
    // // make post request
    // $.ajax({
    // url: url,
    // dataType: 'json',
    // type: 'POST',
    // data: JSON.stringify(data),
    // contentType: 'application/json; charset=utf-8',
    // success: function(data){
    //     alert(data.message);
    // }.bind(this),
    // error: function(xhr, status, err){
    //     alert('Poll creation failed: ' + err.toString());
    // }.bind(this)
    // });
}
render() {
    var classContext = "col-md-6 col-sm-offset-3"
    var all_options = this.state.all_options.map(function(option){
        return(<option key={option.id} value={option.name} />)
    });

    return (
    <div className="container">
            <div className='row'>
            <form id="poll_form" className="form-signin mx-auto" onSubmit={this.handleSubmit}>
                <div className="row">
                <h2 className="mx-auto" >Create a poll</h2></div>

                <div className="form-group has-success">
                <label htmlFor="title" className="sr-only">Title</label>
                <input type="text" id="title" name="title" className="form-control" placeholder="Title" onChange={this.handleTitleChange} required autoFocus autoComplete="off"/>
                </div>

                <div className="form-group has-success">
                <label htmlFor="option" className="sr-only">Option</label>
                <input list="option" className="form-control" placeholder="Option" onChange={this.handleOptionChange}
                value={this.state.option ? this.state.option: ''} autoFocus />
                </div>

                <datalist id="option">
                {all_options}
                </datalist>

                <div className="form-group has-success">
                <label htmlFor="option" className="sr-only">datetime</label>
                
                </div>
                <br />
                <div className="row form-group">
                <button className="btn btn-lg btn-success btn-block" type="button" onClick={this.handleOptionAdd}>Add option</button>
                <button className="btn btn-lg btn-success btn-block" type="submit">Save poll</button>
                </div>
                <br />
            </form>
            </div>
            <div className="row">
                <h4 className="mx-auto">Live Preview</h4>
            </div>
            <div className="row">
                <LivePreview title={this.state.title} options={this.state.options} classContext={classContext} />
            </div>
    </div>
    );
    }
}

export default PollForm;