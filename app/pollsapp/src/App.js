import React from 'react';
import {Link,Switch,Route,NavLink,useRouteMatch} from 'react-router-dom';
import MainMenu  from './menus/MainMenu';
import logo from './logo.svg';
import './App.css';

import BasicLayout from './layout';
import RoutesConfig from './route_config';

 
const Item = () => {
  const { name } = useParams();

  return (
    <div>
      <h3>{name}</h3>
    </div>
  );
}

const Category = () => {
  const { url, path } = useRouteMatch();
  return (
    <div>
      <ul>
        <li>
          <Link to={`${url}/shoes`}>Shoes</Link>
        </li>
        <li>
          <Link to={`${url}/boots`}>Boots</Link>
        </li>
        <li>
          <Link to={`${url}/footwear`}>Footwear</Link>
        </li>
      </ul>
      <Route path={`${path}/:name`}>
        <Item />
      </Route>
    </div>
  );
};

class App extends React.Component {
  constructor(props){
    super(props);
    this.state=({user:''})
  }

  render(){
    return (
      <BasicLayout className="App">
        <Switch>
 
        <RoutesConfig/>
        {/* <Route exact path="/"><HomeRender/></Route>
        <Route exact path="/home"><HomeRender/></Route>
        <Route path="/search"><Search/></Route>
        <Route path="/category"><Category/></Route>
        <Route path="/polls"><PollsPage></PollsPage></Route>
        <Route path="/login" component={Login}></Route>
        <Route path="/signup"><Signup></Signup></Route> */}
        </Switch>
      </BasicLayout>
    );
  }
}

export default App;
