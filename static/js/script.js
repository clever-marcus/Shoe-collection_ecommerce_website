var updateBtns = document.getElementsByClassName('update-cart');

for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        let productId = this.dataset.product
        let action = this.dataset.action
        console.log('productId:', productId, 'Action:', action)

        console.log('USER: ', user)
        if (user === 'AnonymousUser') {
            console.log("User is Not authenticated")

        } else {
            updateUserOrder(productId, action)
        }

    })
}



function updateUserOrder(productId, action) {
    console.log('User is authenticated, sending data...')

    let url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    })

        .then((response) => {
            return response.json()
        })

        .then((data) => {
            console.log('data:', data)
            location.reload()
        })
}

//select toggle dark/light mode button
let toggle = document.getElementById("mode");

toggle.addEventListener('click', () => {
    document.body.classList.toggle('dark');
})

let menu = document.querySelector('#menu-bar');
let navbar = document.querySelector('.navbar');

menu.onclick = () => {
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
}

window.onscroll = () => {
    menu.classList.remove('fa-times');
    navbar.classList.remove('active');
}



