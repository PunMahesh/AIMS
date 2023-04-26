class Header extends HTMLElement {
    constructor() {
        super();

    }

    connectedCallback() {
<<<<<<< HEAD
        this.innerHTML = `
=======
        this.innerHTML = 
>>>>>>> Master
            <header>
                <div class="header-div">
                <div class ="header-div-content">
                    <div class="logo-container">
<<<<<<< HEAD
                        <img src="static/assets/images/logo.png" alt="logo"/>
=======
                        <img src="../../assets/images/logo.png" alt="logo"/>
>>>>>>> Master
                    </div>
                    <div class="nav-items-container">
                        <nav>
                            <ul class="nav-ul">
                                <li>Home</li>
                                <li>Blogs</li>
                                <li>Farmers Kit</li>
                                <li>Market</li>
                                <li>Hire</li>
                                <li>Account</li>
                            </ul>
                        </nav>
                    </div>
                    <div class="cart-search-container">
<<<<<<< HEAD
                        <img src="static/assets/images/search.png" alt="search-button"/>
                        <img src="static/assets/images/shopping-bag.png" alt="cart-button"/>
=======
                        <img src="../../assets/images/search.png" alt="search-button"/>
                        <img src="../../assets/images/shopping-bag.png" alt="cart-button"/>
>>>>>>> Master
                    </div>
                    </div>
                </div>
            </header>
<<<<<<< HEAD
        `
=======
        
>>>>>>> Master
    }
}

customElements.define("header-element", Header);