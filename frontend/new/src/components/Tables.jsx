import React from "react";

const Tables = (props) => {
    return(
        <>
            <table>
                <thead>
                    <tr>
                        <th>{props.stock_name} </th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>S.no</td>
                        <td>Stock Name</td>
                        <td>Transaction Type</td>
                        <td>Stock Units</td>
                        <td>Stock Price</td>
                        <td>Date</td>
                    </tr>
                    <tr>
                        <td>{props.no}</td>
                        <td>{props.stock_name}</td>
                        <td>{props.transaction_type}</td>
                        <td>{props.no_of_stocks}</td>
                        <td>{props.price_of_stock}</td>
                        <td>{props.transaction_date}</td>
                    </tr>
                </tbody>
            </table>
            <br />
                <br />

        </>

    )
}

export default Tables;