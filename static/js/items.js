var subItems = document.querySelectorAll('.item');
subItems[0].style.color = '#0072C6';
for (var i = 0; i < subItems.length; i++) {
    var item = subItems[i];
    item.addEventListener('click', function (event) {
        var activeElment = document.querySelector('.active');
        if (activeElment !== null) {
            activeElment.classList.remove('active');
            activeElment.style.color = 'black';
        }
        this.classList.add('active');
        this.style.color = '#0072C6';
    });
}