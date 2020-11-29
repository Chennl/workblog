
import {Link,Switch,Route,NavLink,useRouteMatch} from 'react-router-dom';
//导入组件
import AntdHome from './layout';
import Login from './users/Login';
import Signup from './users/Signup';
import Home from './Home';
import Search from './searchbox/Search.js';
import PollsPage from './polls/PollsPage';
import Poll from './polls/Poll'
import AllPolls from './antd/polls/AllPolls'
import PollForm from './antd/polls/PollForm'
function Logout(){
  return (<div>logout</div>);
}

function RoutesConfig(){
  return(<div>
    <Route path="/" exact component={Home}></Route>
    <Route path="/home" component={AntdHome}></Route>
    <Route exact path="/polls" component={AllPolls}></Route>
    <Route path="/polls/create" component={PollForm}></Route>
    <Route path="/login" component={Login}></Route>
    <Route path="/logout" component={Logout}></Route>
    <Route path="/signuo" component={Signup}></Route>
    </div>
  );
}

export default RoutesConfig;
  
  
