let subItems = document.querySelectorAll('.item');
subItems[0].style.color = '#0072C6';
for (let i = 0; i < subItems.length; i++) {
    let item = subItems[i];
    item.addEventListener('click', function (event) {
        let activeElment = document.querySelector('.sub-nav-active');
        if (activeElment !== null) {
            activeElment.classList.remove('sub-nav-active');
            activeElment.style.color = 'black';
        }
        event.target.classList.add('sub-nav-active');
        this.style.color = '#0072C6';
    });
}
