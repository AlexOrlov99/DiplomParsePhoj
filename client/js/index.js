window.oncontextmenu = function(event){
    event.preventDefault()
}

let refreshToken = localStorage.getItem('refresh')
let formAuthorization = document.forms.authorization

if (formAuthorization) {
    if (refreshToken) {
        location.href='/main/index.html'
    } else {
        authorizationUser()
    }
}

function mainContent(){
    formAuthorization.classList.add('disable')
    document.querySelector('main').classList.remove('disable')
   
}

function authorizationUser(){
    formAuthorization.addEventListener('submit', (e) => {
        e.preventDefault()
        let formData = new FormData(formAuthorization)
        let xhr = new XMLHttpRequest()
        xhr.open('POST', 'http://localhost:8000/api/v1/token/')
        xhr.responseType = 'json'
        xhr.send(formData)

        xhr.onload = () => {
            if(xhr.status != 200 && xhr.readyState != 4){
                console.log(`Error. Status: ${xhr.status} 
                    <=> ${xhr.statusText} <==> ${xhr.readyState}`);
            }else{
                console.log(`Complete connect: ${xhr.status}`);
                let tokens = xhr.response
                if(tokens.access){
                    localStorage.setItem('access', tokens.access)
                }
                if(tokens.refresh){
                    localStorage.setItem('refresh', tokens.refresh)
                }
                location.href='/main/'
            }
        }
    })
}

