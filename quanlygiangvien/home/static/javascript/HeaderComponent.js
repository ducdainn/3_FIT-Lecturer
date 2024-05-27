function toggleDropdown() {
    const dropAccount = document.getElementById("box_drop_account");
    dropAccount.classList.toggle("active_drop_box");
    dropAccount.classList.toggle("unactive_drop_box");
}

document.addEventListener("click", function(event) {
    const dropAccount = document.getElementById("box_drop_account");
    const accountDropdown = document.getElementById("account_dropdown");
    if (!dropAccount.contains(event.target) && !accountDropdown.contains(event.target)) {
        dropAccount.classList.remove("active_drop_box");
        dropAccount.classList.add("unactive_drop_box");
    }
});