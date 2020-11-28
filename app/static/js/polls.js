const {
  colors,
  CssBaseline,
  ThemeProvider,
  Typography,
  Container,
  makeStyles,
  createMuiTheme,
  Box,
  SvgIcon,
  Button,
//  Link,
} = MaterialUI; 

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
        var url = origin +"/api/options";
        console.log('componentDidMount',url)
        $.ajax({
            url: url,
            dataType: 'json',
            cache: false,
            success: function(data) {
              this.setState({all_options: [...data]});
               
            }.bind(this),
            error: function(xhr, status, err) {
              console.error(url, status, err.toString());
            }.bind(this)
          });
    }

    handleOptionAdd(){
        console.log('handleOptionAdd');
        //update poll options and reset options to an empty string
        this.setState({
            options: this.state.options.concat({name: this.state.option}),
            option: ''
        });

    }
    handleOptionChange(e){
        console.log('handleOptionChange',e)
        this.setState({option: e.target.value});
    }
    handleTitleChange(e){
        //change title as the user types
        this.setState({title: e.target.value});
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

        // make post request
        $.ajax({
        url: url,
        dataType: 'json',
        type: 'POST',
        data: JSON.stringify(data),
        contentType: 'application/json; charset=utf-8',
        success: function(data){
            alert(data.message);
        }.bind(this),
        error: function(xhr, status, err){
            alert('Poll creation failed: ' + err.toString());
        }.bind(this)
        });
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
                    <input type="text" id="title" name="title" className="form-control" placeholder="Title" onChange={this.handleTitleChange} required autoFocus />
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

class LivePreview extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            selected_option:'',
            disabled:0
        }
    }
    handleOptionChange(e){
        this.setState({selected_option: e.target.value });
    }
    
    voteHandler( e ){
        e.preventDefault();
    
        var data = {"poll_title": this.props.title, "option": this.state.selected_option};
    
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
            }
        });
        console.log(options)
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

class AllPolls extends React.Component {
    render() {
        return (
          <div>
            app polls
          </div>
        );
      }
  }

 
class Square extends React.Component{
    constructor(props){
        super(props);
        this.state = { 
            value:null
        };
    }

    render(){
        return (
            <button 
                className="square" 
                onClick={( )=> this.setState({value: 'X'})}
            >
                {this.state.value}
            </button>
        )
    }
}

class Clock extends React.Component {
    constructor(props) {
        super(props);
        this.state = {date: new Date()};
        console.log('constructor')
    }

    componentDidMount() {
        console.log('componentDidMount')
        this.timerId = setInterval(
            ()=>this.tick(),
            1000
        );
    }
  
    componentWillUnmount() {
        console.log('componentWillUnmount')
        clearInterval()
    }

    tick(){
        this.setState({
            date: new Date()
        });
    }
    render() {
      return (
        <div>
          <h1>Hello, {this.props.author}!</h1>
          <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
          <Square value="乘法" />
        </div>
      );
    }
}


 

const Link = ReactRouterDOM.Link,
      Route = ReactRouterDOM.Route;
 

    //   ( <ReactRouterDOM.HashRouter>
    //     <ul>
    //       <li><Link to="/">TO HOME</Link></li>
    //       <li><Link to="/a">TO A</Link></li>
    //       <li><Link to="/b">TO B</Link></li>
    //     </ul>

    //     <Route path="/" exact component={PollForm} />
    //     <Route path="/a" component={Clock} />
    //     <Route path="/b" component={Square} />
    //   </ReactRouterDOM.HashRouter>)

ReactDOM.render( 
    ( <ReactRouterDOM.HashRouter>
      
        <Route path="/" exact component={PollForm} />
        <Route path="/a" component={Clock} />
        <Route path="/b" component={Square} />
      </ReactRouterDOM.HashRouter>)
  ,
    document.getElementById('container')
);


