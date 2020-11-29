import React from 'react'
import './SearchBox.css'

class SearchBox extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            keyword:'',
            isSearchShow:true,
            color:25,
        };
        this.handleChange = this.handleChange.bind(this);
        this.onSearchClick = this.onSearchClick.bind(this);

        
       this.input = React.createRef();
    }
    handleChange(e){
        this.setState({keyword: '['+e.target.value+']'});
    }
    onSearchClick(e){
        this.props.searchKeyword(this.state.keyword);
        //此时input可以通过ref进行DOM操作，称为非受控组件。虽然这种模式打破了数据驱动view的原则，但是有时候还是比较方便的，比如获取滚动条的高度。
        //this.setState({searchVal:this.input.current.value});

    }
    render(){
        //定义color变量，并根据状态显示不同的颜色
        let color;
        if(this.state.color<10){
            color="green"
        }else if(this.state.color<20){
            color="blue"
        }else if(this.state.color<30){
            color="red"
        }else{
            color="orange"
        }


        return (
            <div style={{width:300,margin:10}} className='search_box'>
                <input type="text" style={{width:150}}  onChange={this.handleChange} value={this.state.keyword } ref={this.input}></input>&nbsp;&nbsp;
                <button onClick={this.onSearchClick} disabled={this.state.isSearchShow ?"":"disabled"} style={{backgroundColor:color}} >搜索</button>
            </div>
        )
    }
}
export default SearchBox;
