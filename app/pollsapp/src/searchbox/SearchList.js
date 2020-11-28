import React from 'react'
import './SearchList.css'

class SearchList extends React.Component{
    constructor(props){
        super(props);
        this.searchul = React.createRef();
        this.state = {searchResults:['电脑','电视','冰箱']};
    }
/*     static getDerivedStateFromProps(nextProps,preState){

        console.log("preState",preState);
        console.log("nextProps",nextProps);

        if(nextProps.searchResults !== preState.searchResults 
                && nextProps.searchResults.length){
                   
                    return {searchResults : nextProps.searchResults };
        }
        return null;
    } */
    
    render(){
        let results = this.props.searchResults.map((value)=>(
            <li key={value.toString()} >{value}</li>
        ));
       
        return (
            <div>
                <div className="search-header">
                    <span>搜索结果:</span>
                </div>
                <div className="search-body" ref={this.searchul} >
                    {this.props.children}
                    <ul>

                       {results}
                    </ul>
                </div> 
            </div>
        );
    }
}

export default SearchList;