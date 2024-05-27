/* This JavaScript code snippet is adding event listeners to certain elements on the page when the DOM
content has finished loading. Here's a breakdown of what the code is doing: */
document.addEventListener("DOMContentLoaded", function () {
    const editButtons = document.querySelectorAll("#btn_upd");

    editButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            try {
                const row = this.closest("tr");
                const cells = row.getElementsByTagName("td");

                const instructorID = this.getAttribute('data-instructor-id');
                document.getElementById("instructorID_edit").value = instructorID;

                document.getElementById("avt_preview").src = cells[1].dataset.imageUrl;
                document.getElementById("name_edit").value = cells[2].textContent;
                document.getElementById("department_edit").value = cells[12].textContent;
                document.getElementById("status_edit").value = cells[4].textContent;
                document.getElementById("gender_edit").value = cells[5].textContent;
                document.getElementById("birthdate_edit").value = cells[6].textContent;
                document.getElementById("phonenumber_edit").value = cells[7].textContent;
                document.getElementById("placeoforigin_edit").value = cells[8].textContent;
                document.getElementById("email_edit").value = cells[9].textContent;
                document.getElementById("education_edit").value = cells[10].textContent;
                document.getElementById("position_edit").value = cells[11].textContent;
            } catch (e) {
                console.error("Error while processing the row data: ", e);
            }
        });
    });



    const deleteButtons = document.querySelectorAll("#btn_del");

    deleteButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            const instructorID = this.getAttribute('data-instructor-id');
            const deleteConfirmationModal = document.getElementById("deleteConfirmationModal");
            const instructorIdInput = deleteConfirmationModal.querySelector("#instructor_id");
            instructorIdInput.value = instructorID;
            console.log("Instructor ID for deletion:", instructorID); // Log để kiểm tra
        });
    });

    // Xóa bài viết
    const deletePostButtons = document.querySelectorAll("#btn_del_post");

    deletePostButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            const articleID = this.getAttribute('data-article-id');
            const deletePostConfirmationModal = document.getElementById("deletePostConfirmationModal");
            const articleIDInput = deletePostConfirmationModal.querySelector("#post_id");
            articleIDInput.value = articleID;
            console.log("Article ID for deletion:", articleID); // Log để kiểm tra
        });
    });



    

    
});
