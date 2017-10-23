window.onload = function () {
    var subItems = document.querySelectorAll('.sub-item');
    for (var i = 0; i < subItems.length; i++) {
        var item = subItems[i];
        item.addEventListener('click', function (event) {
            var activeElment = document.querySelector('.active');
            if (activeElment !== null) {
                activeElment.classList.remove('active');
                activeElment.style.color = '#fff';
            }
            this.classList.add('active');
            this.style.color = '#969696';
        });
    }
};