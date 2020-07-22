import React from 'react';

class Box extends React.Component {
  constructor(boxClass){
    super();
    this.class = boxClass;
  }
  render(){
    return (<div className={this.class}></div>)
  }
}

export default Box;