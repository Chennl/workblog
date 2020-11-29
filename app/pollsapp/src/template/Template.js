
 
import MainMenu from '../menus/MainMenu';
 
export const Template = (props) => (
    <div className = 'page'>
      <MainMenu></MainMenu>
      {props.children}
    </div>
  )