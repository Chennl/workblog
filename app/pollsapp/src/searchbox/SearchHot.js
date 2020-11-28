import React from 'react'
import './SearchHot.css'

class SearchHot extends React.Component{
    constructor(props){
        super(props);
        this.state ={hotItem:['口罩','手套','酒精']};
        //this.changeHot = this.changeHot.bind(this);

    }
    // 在箭头函数中，this指向的函数的本身，而不是函数的调用者，可以参考ES6系列教程第八篇--箭头函数详解
    //https://blog.csdn.net/tcy83/article/details/104574855
    changeHot = (e) =>{
        e.preventDefault();
        e.stopPropagation();
        this.setState({hotItem:['电视','手机','电脑','平板']});
    }
    render(){
        const hotList = this.state.hotItem.map((value)=>(
            <li key={value.toString()} className="hotlist">
                {value}
            </li>
        ))
        return (
            <div className="hot-container">
                <div className="hot-header">
                    <span>大家都在搜:</span><a href='search.json' onClick={this.changeHot} style={{marginLeft:100}}>下一批</a>
                </div>
                <div className="hot-body">
                    <u >
                        {hotList}
                    </u>
                </div>
            </div>
        );
    }
}

export default SearchHot;