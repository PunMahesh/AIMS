class Header extends HTMLElement {
    constructor() {
        super();

    }

    connectedCallback() {
        this.innerHTML = `
            <header>
                <div class="header-div">
                <div class ="header-div-content">
                    <div class="logo-container">
                        <img src="static/assets/images/logo.png" alt="logo"/>
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
                        <img src="static/assets/images/search.png" alt="search-button"/>
                        <img src="static/assets/images/shopping-bag.png" alt="cart-button"/>
                    </div>
                    </div>
                </div>
            </header>
        `
    }
}

customElements.define("header-element", Header);