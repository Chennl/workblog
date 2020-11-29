import React from 'react'
import { useRouteMatch } from 'react-router-dom/cjs/react-router-dom.min';
import {Link,Switch,Route,NavLink,Redirect}  from 'react-router-dom';
 
import Poll from './Poll'
import AllPolls from './AllPolls'
import PollForm from './PollForm'

const activeStyle = {  fontWeight: "bold"   }

//const PollsIndex =()=>{  const { path } = useRouteMatch();console.log(path); return(<div><h3>嵌套路由主页</h3><Link to={`${path}/signin`}>登录</Link></div>);}

const PollsPage =()=>{
    
    const { url, path,history } = useRouteMatch();

    return (
        <nav>
            <ul className="nav">
                <li className="nav-item">
                    <NavLink to={`${url}/list`} className="nav-link" activeStyle={activeStyle} >Poll Station</NavLink>
                </li>
                <li className="nav-item">
                    <NavLink to={`${url}/create`} className="nav-link" activeStyle={activeStyle} >Creat A Poll</NavLink>
                </li>
                <li className="nav-item">
                    <NavLink to={`${url}/view`} className="nav-link" activeStyle={activeStyle} >Poll</NavLink>
                </li>
            </ul>
            <Switch>
                <Route exact path={path}><Redirect to={`${path}/list`}></Redirect></Route>
                <Route exact path={`${path}/poll`} component={()=>{console.log(path); return(<Poll/>);}}/>
                <Route exact path={`${path}/create`} component={PollForm}/>
                <Route  path={`${path}/list`} component={AllPolls}/>
                <Route  path={`${path}/:pollName`} component={AllPolls}/>
            </Switch>
        </nav>
       

        )
 
}

export default PollsPage;