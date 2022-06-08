import React from "react";
import {BrowserRouter as Router,Route,Routes} from "react-router-dom";
import NavBarMenu from "./NavBarMenu";
import StockAdd from "./StockAdd";
import StockList from "./StockList";
import Individuals from "./Individuals";
import Overall from "./Overall";

const Main = () => {
    
return(
        <>
        <NavBarMenu />
            <div>
                <Router>
                    <Routes>
                        <Route exact path="/" element={<StockList />} />
                        <Route exact path="/addStock" element={<StockAdd />} />
                        <Route exact path="/individual" element={<Individuals />} />
                        <Route exact path="/overall" element={<Overall />} />
                        
                    </Routes>
                </Router>
                
            </div>
            
            <br>
            </br>

        </>
    )
}

export default Main;