import React from 'react'
import SearchBox from './SearchBox.js';
import SearchList from './SearchList.js';
import SearchHot from './SearchHot.js';

class Search extends React.Component{
    constructor(props){
        super(props);
        this.state=({searchResults:['牛奶','饼干']})
        this.handleSearch = this.handleSearch.bind(this);
      }
    handleSearch(keyword){
        console.log("输入值:"+keyword);
        let result=['牛奶','饼干'];
        this.setState({searchResults:['牛奶','饼干']});
    }
    render(){
        return (
            <div>
                <SearchBox searchKeyword={this.handleSearch}/>
                <SearchHot/>
                <SearchList searchResults={this.state.searchResults}>
                <div>为您搜索到{this.state.searchResults.length }条记录</div>
                </SearchList>
            </div>
        )
    }
}
export default Search;
