document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById('createForumModal');
    var btn = document.querySelector('.btn_create_forum');
    var span = document.querySelector('.close');

    btn.onclick = function() {
        modal.style.display = 'block';
    }

    span.onclick = function() {
        modal.style.display = 'none';
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
});