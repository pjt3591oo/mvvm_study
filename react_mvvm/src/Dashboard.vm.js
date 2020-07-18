import { 
  ViewModel,
  ViewAware,
} from 'react-mvvm';
import Dashboard from './Dashboard';
 
class DashboardVM extends ViewAware {
 
  // Functional class properties, automatically passed as view props.
 
  sayHello = () => {
    alert('Hello, my little friend.');
  };
 
  sayGoodbye = () => {
    alert('Goodbye!');
  };
 
  // Prototype methods are NOT passed as view props.
 
  componentDidMount() {
    console.log('DashboardVM.componentDidMount');
  }
  
  componentDidUpdate(prevProps, prevState, prevContext) {
    console.log('DashboardVM.componentDidUpdate');
  }
 
  componentWillUnmount() {
    console.log('DashboardVM.componentWillUnmount');
  }
 
  // However, if you wish to call a prototype method from the view,
  // the entire DashboardVM class instance is passed to the view as
  // `props.vm`.
 
  doSomethingElse() {
    return () => {
      alert('Doing something else...');
    };
  }
 
}
 
export default ViewModel.connect(
  DashboardVM, 
  Dashboard
);