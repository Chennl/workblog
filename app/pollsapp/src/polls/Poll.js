import React from 'react'

class Poll extends React.Component{
    constructor(props){
        super(props);
        this.state = { isSubmited:false}
    }
    render(){
        return (
            <div className="container">
                <div className="row">
                    <p> do poll</p>
                </div>
            </div>
        )
    }
}

export default Poll;