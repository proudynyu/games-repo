import React from 'react';

class Box extends React.Component {
  constructor(boxClass, width){
    super();
    this.boxClass = `${boxClass}`;
    this.width = `${width}`
  }
  render(){
    return (
      <div 
        className={this.props.boxClass}
        width={this.props.width}
      >
      </div>
    )
  }
}

export default Box;