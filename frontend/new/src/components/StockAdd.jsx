import React,{ useEffect, useState } from "react";
import axios from "axios";
import "./date.css";
import { useNavigate } from 'react-router-dom';


const StockAdd = () => {
    const navigate = useNavigate();
    const [stocks,Setstocks] = useState([]);
    const [name,Setname] = useState("");
    const [type,Settype] = useState("");
    const [unit,Setunit] = useState();
    const [price,Setprice] = useState();
    const [date,Setdate] = useState("");

//    const datereversal = (dates) => {
//        let date = dates
//        let date1 = date.split("-")
//        console.log(date1)
//        date1.shift()
//        console.log(date1)
//        let date2 = date1[0]+"-" +date1[1] + "-" + date.slice(0,4)
//        console.log(date2)
//        return date2
//  }
     


    const getProducts = async() => {
        const response = await axios.get("http://127.0.0.1:8000/company")
        console.log(response.data)
        Setstocks(response.data)
    }
    const AddStockInfo = async() => {
            //   let formField = new FormData()
            //   formField.append('stock_name',name)
            //   formField.append('transaction_type',type)
            //   formField.append('no_of_stocks',unit)
            //   formField.append('price_of_stock',price)
            //   formField.append('transaction_date',date)
               await axios({
                 method:'post',
                 url:'http://127.0.0.1:8000/api/',
                 headers: {
                          'Content-Type': 'application/json'
                 },
                 data: {
                    "stock_name": name,
                    "transaction_type": type,
                    "no_of_stocks": unit,
                    "price_of_stock": price,
                    "transaction_date": date
                }
                   }).then((response) => {
                    console.log(response.data)
                    navigate('/');
                   })
            // await  axios.post('http://127.0.0.1:8000/api/',
                // data : fo
                    // .then(res => console.log(res))
                    // .catch(err => console.log(err));
        //    

        // fetch('http://127.0.0.1:8000/api/', {
        //     method: 'post',
        //     headers: {
        //         'Accept': 'application/json',
        //         'Content-Type': 'application/json'
        //   },
        //     body: {
        //             stock_name : name,
        //             transaction_type : type,
        //             no_of_stocks : unit,
        //             price_of_stock : price,
        //             transaction_date : date
        //     }
        //   })
        //     .then(function(response) {
        //         return response.json()
        //       }).then(function(body) {
        //         console.log(body);
        //       });


    }
    useEffect(() => {
        getProducts()
    },[])
    return(
        
        <>
            <br /> <br /> <br />

            <div className="form-group">
                <p>Choose Stock</p>
                <select value={name} onChange={(event) => {
                    console.log(typeof event.target.value)
                    Setname(event.target.value)
                }} >
                    {stocks.map(stock => (
                        <option value={stock.name} >{stock.name}</option>
                    ))}
                </select>    
                
            </div>
            <br />
            <div className="form-group">
                <p>Transaction Type</p>
                <select value={type} onChange={(event) => {
                    console.log(typeof event.target.value)
                    Settype(event.target.value)
                }} >
                    <option value="BUY" >BUY</option>
                    <option value="SELL" >SELL</option>
                </select>
                </div>
                <br />


                <div className="form-group">
                <label for="formGroupExampleInput2">Units Of Stock</label>
                <input type="text" class="form-control" value={unit} onChange={(event) => {
                    console.log(typeof event.target.value)
                    Setunit(event.target.value.toString())
                }} placeholder="Price of Stock" />
              </div>

              <div className="form-group">
                <label for="formGroupExampleInput2">Price Of Stock</label>
                <input type="text" class="form-control" value={price} onChange={(event) => {
                    console.log(typeof event.target.value)
                    Setprice(event.target.value)
                }} placeholder="Price of Stock" />
              </div>
              <label for="start">Transaction Date:</label>

                <input type="date" id="start" name="trip-start"
                    value="" onChange={(event) => {
                        console.log(typeof event.target.value)
                        Setdate(event.target.value)
                    }} min="2000-01-01" max="2100-12-31"></input> <br /> <br />

              <button type="submit" onClick={AddStockInfo} class="btn btn-primary">Add Stock</button>
                     
        </>
    )
};

export default StockAdd;