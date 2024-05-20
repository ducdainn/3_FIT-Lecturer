function HeaderComponent() {
    const header = document.getElementById("header_component")


    const template = `
        <div class="header">
            <div>
                <h2>TEACH TRACK</h2>
            </div>
            <div class="box_control">
                <div>
                    <i class="fa-sharp fa-solid fa-bell"></i>
                </div>
                <div>
                    <i class="fa-solid fa-envelope"></i>
                </div>
                <div>
                    <i class="fa-solid fa-user"></i>
            
                </div>
            
            </div>
        </div>
    `;
    header.innerHTML = '';
    header.insertAdjacentHTML("beforeend", template);

}

HeaderComponent();