import React from "react";


const Dashcard = (props) => {
    return(
                <div class="card">
                    <div class="card-header">
                        Overall Stock Dashboard
                    </div>
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item">Total Investment : {props.inv} </li>
                        <li class="list-group-item">Total Stock Unit : {props.uni} </li>
                        <li class="list-group-item">Total Current Amount : {props.cu} </li>
                        <li class="list-group-item">Overall Profit : {props.pro} </li>
                    </ul>
                </div>
    )
};

export default Dashcard;