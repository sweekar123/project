import React,{useState,useEffect} from "react";
import axios from 'axios';
import Tables from "./Tables";

const StockList = () => {
    const [stocks,Setstocks] = useState([])

    const getStocks = async() => {
        const response = await axios.get("http://127.0.0.1:8000/api")
        console.log(response.data)
        Setstocks(response.data)
    }

    useEffect(() => {
        getStocks();
    },[])

    return(
            <>
                <div>
                    {
                        stocks.map((stock,index) => (
                            <Tables key={stock.id}
                                    no = {stock.id}
                                    stock_name = {stock.stock_name}
                                    transaction_type = {stock.transaction_type}
                                    no_of_stocks = {stock.no_of_stocks}
                                    price_of_stock = {stock.price_of_stock} 
                                    transaction_date= {stock.transaction_date}
                                    />
                        ))
                    }
                </div>
            </>
    )
};
export default StockList;
