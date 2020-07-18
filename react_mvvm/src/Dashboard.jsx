import React from 'react';
import MVVM from 'react-mvvm';
 
export default class Dashboard extends MVVM.ViewComponent {
  render() {
    return (
      <div>
        <h1>Dashboard</h1>
        <p>
          Welcome.
        </p>
        {/* <button onClick={this.props.sayHello}>
          Say Hello
        </button>
        <button onClick={this.props.sayGoodbye}>
          Say Goodbye
        </button>
        <button onClick={this.props.vm.doSomethingElse()}>
          Do Something Else
        </button> */}
      </div>
    );
  }
  /*
  constructor(props) {
    super(props);
    // You can also just forward events instead of inheriting ViewComponent.
    ViewComponent.forwardEvents(this, props.vm);
  } // */
}