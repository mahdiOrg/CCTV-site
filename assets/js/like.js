function like(product_id) {
    var heart = document.getElementById('heart')
    var count = document.getElementById('count')
    console.log(count.innerText)
    $.get(`/products/like/${product_id}`).then(response => {
        if (response['response'] === 'liked') {
            count.innerText = Number(count.innerText) + 1;
            heart.className = 'bi bi-heart-fill';
        } else {
            count.innerText = Number(count.innerText) - 1;
            heart.className = 'bi bi-heart';

        }

    })
}