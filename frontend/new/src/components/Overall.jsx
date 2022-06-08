import React,  { useEffect, useState } from "react";
import axios from "axios";
import Dashcard from "./Dashcard";


const Overall = () => {
    const [stocks,Setstocks] = useState([]);
    let units = 0;
    let investment = 0;
    let current_amount = 0;
    let profit = 0;



    useEffect(() => {
        const getProducts = async() => {
            const response = await axios.get("http://127.0.0.1:8000/api")
            console.log(response.data)  
            Setstocks(response.data)
        }
        
        getProducts();
    },[])

    return(
        <>

            { stocks.map(stock => {
                 units = units + stock.no_of_stocks
                 investment = investment + stock.no_of_stocks * 100
                 current_amount = current_amount + stock.no_of_stocks * Number(stock.price_of_stock)
                 console.log(units)
                 profit = profit + stock.no_of_stocks * Number(stock.price_of_stock) - stock.no_of_stocks * 100
            })
            }
            <Dashcard inv = {investment}
                      uni = {units}
                      cu = {current_amount}
                      pro = {profit}
                       />

        </>
    )
};

export default Overall;