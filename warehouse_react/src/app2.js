/**
 * Created by leszek on 22.03.18.
 */

import React from 'react';
import { Provider } from 'react-redux';
import './index.css';
import WarehouseSFIList from './components/ItemsList';
import { BrowserRouter as Router,Switch, Route, Link } from 'react-router-dom';
import App from './App'
import Menu from './components/Menu'
import ItemDetail from './components/ItemDetail';

class App2 extends React.Component {
    render() {
        return (
            <Router>

                <div className="container">

                    <Route exact path="/" component={App}/>

                        <Route path="/semi-finished-item" component={WarehouseSFIList} />

                        <Route path="/semi-finished-item-detail/:id" component={ItemDetail}/>

                </div>
            </Router>
        );
    }
}

export default App2;