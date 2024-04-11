document.addEventListener("DOMContentLoaded", function () {
    const editButtons = document.querySelectorAll(".edit-button");

    editButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            const row = this.closest("tr");
            const cells = row.getElementsByTagName("td");
            const instructorID = this.getAttribute('data-instructor-id');
            document.getElementById("instructorID_edit").value = instructorID; 
            document.getElementById("name_edit").value = cells[2].textContent;
            document.getElementById("gender_edit").value = cells[3].textContent;
            document.getElementById("birthdate_edit").value = cells[4].textContent;
            document.getElementById("phonenumber_edit").value = cells[5].textContent;
            document.getElementById("placeoforigin_edit").value = cells[6].textContent;
            document.getElementById("email_edit").value = cells[7].textContent;
            document.getElementById("department_edit").value = cells[8].textContent;
            document.getElementById("education_edit").value = cells[9].textContent;
            document.getElementById("position_edit").value = cells[10].textContent;
            document.getElementById("status_edit").value = cells[11].textContent;
        });
    });
});
