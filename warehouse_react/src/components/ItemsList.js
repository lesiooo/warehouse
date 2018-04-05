/**
 * Created by leszek on 20.03.18.
 */
import React from 'react';
import {BrowserRouter as Router, Route, Link} from 'react-router-dom';
import ItemDetail from './ItemDetail';
import fetch from 'isomorphic-fetch';
import axios from 'axios';
class WarehouseSFIList extends React.Component {

    constructor() {
        super();
        this.state = {
            'items': [],
            'data': {}
        };
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    componentDidMount() {
        this.getItems();
    }

    getItems(){
        fetch('http://127.0.0.1:8000/warehouse/api/semi-finished-item/')
            .then(results => results.json())
            .then(results => this.setState({'items': results}));
    }
    handleSubmit(event) {
        event.preventDefault();

        axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/warehouse/api/semi-finished-item/',
            data: {
                name: event.target.name.value,
                producer: event.target.producer.value,
                quantity: event.target.quantity.value
            },
            xsrfHeaderName: "X-CSRFToken"
        })
            .then(function (response) {
                console.log(response);
                window.location.reload();
            })
            .catch(function (error) {
                console.log(error);
            })


        console.log('ok');
    }

    renderCreateItem(){
        return(<div className="col-sm-3">
            <form onSubmit={this.handleSubmit}>
                <label>Item name:
                    <input name="name" type="text" className="form-control"/>
                </label>
                <label> Producer:
                    <input name="producer" type="text" className="form-control"/>
                </label>
                <label> Quantity
                    <input name="quantity" type="number" min="0" step="1" className="form-control" />
                </label>
                <button type="submit" className="btn btn-success">Create Item</button>
            </form>
        </div>);
    }

    renderList(){
           return (<div className="col-lg-12">
                   <h2> Item list </h2>
                         <table className="table table-hover">
                             <thead>
                             <tr>
                                 <th>Item name</th>
                                 <th>Producer</th>
                                 <th>Quantity</th>
                                 <th>Detail</th>
                             </tr>
                             </thead>
                            <tbody>{this.state.items.map(function(item, key) {

                               return (
                                  <tr key = {key}>
                                      <td>{item.name}</td>
                                      <td>{item.producer}</td>
                                      <td>{item.quantity}</td>
                                      <td><a href={"/semi-finished-item-detail/" + item.id} ><button type="button" className="btn btn-success">Detail</button></a></td>
                                  </tr>
                                )

                                 })}</tbody>
                           </table>
               </div>

                   );


    }

    render(){
        console.log(this.state.data)
        console.log(JSON.stringify(this.state.data))
        return(

            <div>
                {this.renderCreateItem()}
                {this.renderList()}
            </div>
        );
    }

}

export default (WarehouseSFIList)