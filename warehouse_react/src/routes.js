/**
 * Created by leszek on 20.03.18.
 */
import React from 'react';
import {Router, Route, Link} from 'react-router-dom';
import App from './App';
import WarehouseSFIList from './components/ItemsList';

export default (
    <Router>
        <Route path="/" component={App}/>
        <Route path="/items" component={WarehouseSFIList} />
    </Router>
)