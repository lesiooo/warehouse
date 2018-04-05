/**
 * Created by leszek on 20.03.18.
 */

import React from 'react';
import axios from 'axios';

class ItemDetail extends React.PureComponent {

        constructor(props) {
        super(props);

        this.state = {
            'item': []
        }
        this.handleEdit = this.handleEdit.bind(this);

    }

    getItem(){
        fetch('http://127.0.0.1:8000/warehouse/api/semi-finished-item/' + this.props.match.params.id)
            .then(results => results.json())
            .then(results => this.setState({'item': results}));
    }

    componentDidMount() {
        this.getItem();
    }

    handleEdit(event){
        event.preventDefault();

        axios({
            method: 'put',
            url: this.state.item.url,
            data: {
                name: this.state.item.name,
                producer: this.state.item.producer,
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
    }


    renderEditQuantity() {
        return(
            <div className="col-sm-3">
                <h1> Edit Item</h1>
                <form onSubmit={this.handleEdit}>
                    <label>Quantity
                      <input className="form-control" name="quantity" type="text"/>
                    </label>
                        <button className="btn btn-primary" type="submit"> Edit</button>
                </form>
            </div>
        );
    }

    renderDetail() {
        return(
            <div className="col-sm-3">
                <h1>Item Detail</h1>
                    <p>Name: {this.state.item.name} </p>
                    <p>PRoducer: {this.state.item.producer} </p>
                    <p>Quantity: {this.state.item.quantity} </p>
            </div>

        );
    }
    render() {

        return (


            <div className="form-group">
                {this.renderDetail()}
                {this.renderEditQuantity()}
            </div>
        );
    };
}

export default (ItemDetail)