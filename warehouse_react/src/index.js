import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import './index.css';
import App from './App';
import WarehouseSFIList from './components/ItemsList';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import ReactGA from "react-ga";
import Menu from './components/Menu'
import ItemDetail from './components/ItemDetail';
import App2 from './app2'

import registerServiceWorker from './registerServiceWorker';

registerServiceWorker();
ReactDOM.render(<App2 />, document.getElementById('root'));
ReactDOM.render(<Menu />, document.getElementById('menu'));