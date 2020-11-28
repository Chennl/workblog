import React from 'react';

import {Link,Switch,Route,NavLink}  from 'react-router-dom';

const activeStyle = {  fontWeight: "bold"   }


class MainMenu extends React.Component {
   
    render(){
        var loggedIn =localStorage.getItem('username');
      
        return(
        <nav >
        <ul className="nav">
        <li className="nav-item">
            <NavLink to="/home" className="nav-link" activeStyle={activeStyle} >Home</NavLink>
        </li>
        <li className="nav-item">
            <NavLink className="nav-link"  activeStyle={activeStyle} to="/search">Search</NavLink>
        </li>
        <li className="nav-item">
            <NavLink className="nav-link" activeStyle={activeStyle} to="/category">Category</NavLink>
        </li>
        <li className="nav-item">
            <NavLink className="nav-link" activeStyle={activeStyle} to="/polls">Polls</NavLink>
        </li>
 
        { loggedIn  ?
            <li className="nav-item">
                <NavLink className="nav-link" activeStyle={activeStyle} to="/logout">Logout</NavLink>
            </li>:
             <li className="nav-item">
             <NavLink className="nav-link" activeStyle={activeStyle} to="/login">Login</NavLink>
            </li>
        }
        <li className="nav-item">
            <NavLink className="nav-link" activeStyle={activeStyle} to="/signup">Singup</NavLink>
        </li> 

        </ul>
    </nav>
    )
    }
}

export default MainMenu;