import React from "react";



const NavBarMenu = () => {
    return(
        <>
        <nav class="navbar navbar-expand-lg bg-light">
          <div class="container-fluid">
            <a class="navbar-brand" href="/">Home</a>
            <button class="navbar-toggler"to="/" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
              <ul class="navbar-nav">
                <li class="nav-item">
                  <a class="nav-link active" aria-current="page" href="/">List</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="/addStock">Add Stock</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="/individual">Individual Dashboard</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="overall">Overall Dashboard</a>
                </li>
              </ul>
            </div>
            </div>
        </nav>
</>
)
};

export default NavBarMenu;