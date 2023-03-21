class Footer extends HTMLElement {
    constructor(){
        super();

    }

    connectedCallback(){
        this.innerHTML=`
        <footer class="footer">
        <div class="footer-col">
            <h4>AIMS</h4>
            <div>
                <p>Kathmandu, Nepal</p>
                <p>Phone:+977 9819057663</p>
                <p>Email:info@aims.com</p>
            </div>
        </div>

        <div class="footer-col">
            <h4>USEFUL LINKS</h4>
            <div>
                <p> > Blog</p>
                <p> > News</p>
                <p> > Farmers Kit</p>
                <p> > Farmers Market</p>
            </div>
        </div>

        <div class="footer-col">
            <h4>OUR SERVICES</h4>
            <div>
                <p> > Home</p>
                <p> > About</p>
                <p> > Hire Contact</p>

            </div>

        </div>
    </footer>

        `
    }
}

customElements.define("footer-element",Footer);
