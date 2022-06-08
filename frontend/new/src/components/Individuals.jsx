import axios from "axios";
import React, { useEffect, useState } from "react";
import Cards from "./Cards";


const Individuals = () => {
    const [stocks,Setstocks] = useState([]);

    const getProducts = async() => {
        const response = await axios.get("http://127.0.0.1:8000/api")
        console.log(response.data)
        Setstocks(response.data)
    }
    useEffect(() => {
        getProducts()
    },[])
    return(
        <>
            {
                stocks.map((stock,index) => (
                            <Cards key={stock.id}
                                sno = {index + 1}
                                stock_name = {stock.stock_name}
                                no_of_stocks = {stock.no_of_stocks}
                                price_of_stock = {stock.price_of_stock}
                                transaction_date = {stock.transaction_date} />
                ))
            }

        </>
    )
}

export default Individuals