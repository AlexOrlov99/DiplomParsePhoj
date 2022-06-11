window.oncontextmenu = function(event){
    event.preventDefault()
}

let refreshToken = localStorage.getItem('refresh')
let formAuthorization = document.forms.authorization
let formSendFile = document.getElementById('formfile')
let sendFileBtn = document.getElementById('send_file_btn')
let chooseFile = document.getElementById('choose_file')
let backToPageBtn = document.getElementById('back_to_page')
let modelMain = document.getElementById('modalmain')
let addModalWindow = document.getElementById('addmodalwindow')
let formResume = document.getElementById('form_correct_data')
let sendResumeBtn = document.getElementById('send_resume_btn')

if (formAuthorization) {
    if (refreshToken) {
        mainContent()
    } else {
        authorizationUser()
    }
}

function mainContent(){
    formAuthorization.classList.add('disable')
    document.querySelector('main').classList.remove('disable')
    getResume()
}

async function getResume(){
    let token = `Usr ${localStorage.access}`
    let response = await fetch('http://localhost:8000/api/v1/resume/', {
        method: 'GET',
        headers: {
            'Authorization':token
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        data.forEach(element => {
            document.querySelector('.post').innerHTML += `
            <div class="content">
                <h1>Full name: ${element.full_name}</h1>
                <h2>Email: ${element.email}<h2>
                <h2>Phone: ${element.phone_number}<h2>
            </div>
            `
        });
    })
    .catch(err => {
        console.log(err);
    })
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

                setTimeout(() => {
                    location.reload()
                }, 1000);
            }
        }
    })
}

chooseFile.onclick = function(){
    var file = chooseFile.value;
    if (file.length != 0) {
        file = file.replace (/\\/g, '/').split ('/').pop ()
        abs = 'Имя файла: ' + file
        document.getElementById ('file-name').innerHTML = 'Имя файла: ' + file;
        console.log(file)
    }

}

backToPageBtn.onclick = function(){
    modelMain.style.display = 'none'
    addModalWindow.style.display = 'none'
}

function serializeForm(formNode) {
    const { elements } = formNode
    const data = new FormData()
    Array.from(elements)
      .filter((item) => !!item.name)
      .forEach((element) => {
        const { name, value} = element
        data.append(name, value)
      })
    return data
}

function getDataInValue(form, datafield){
    if (datafield != null){
        form.value = datafield
    }else{
        datafield = datafield.placeholer
    }
}
formSendFile.onsubmit = async(e) => {
    e.preventDefault();
    let response = await fetch('http://localhost:8000/api/v1/resume/pars/',{
        method: 'POST',
        body: new FormData(formSendFile)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.skills)
        modelMain.style.display = 'block'
        addModalWindow.style.display = 'block'
        getDataInValue(formResume.full_name, data.full_name)
        getDataInValue(formResume.email, data.email)
        getDataInValue(formResume.phone_number, data.phone_number)
        getDataInValue(formResume.education, data.education)
        getDataInValue(formResume.experience, data.experience)
        getDataInValue(formResume.skills, data.skills)

        // formResume.full_name.value = data.full_name
        // formResume.email.value = data.email
        // formResume.phone_number.value = data.phone_number
        // formResume.education.value = data.education
        // formResume.experience.value = data.experience
        // formResume.skills.value = data.skills
    
        // data.forEach(element => {
        //     document.querySelector('.post').innerHTML += `
        //     <div class="content">
        //         <h1>Full name: ${element.full_name}</h1>
        //         <h2>Email: ${element.email}<h2>
        //         <h2>Phone: ${element.phone_number}<h2>
        //     </div>
        //     `
        // });
    })
}

sendResumeBtn.onclick = function(){
    formResume.addEventListener('submit', (e) => {
        e.preventDefault()
        let data = serializeForm(formResume)
        let xhr = new XMLHttpRequest()
        xhr.open('POST', 'http://localhost:8000/api/v1/resume/')
        xhr.responseType = 'json'
        xhr.send(data)
        xhr.onload = () => {
            if(xhr.status != 200 && xhr.readyState != 4){
                console.log(`Error. Status: ${xhr.status} 
                    <=> ${xhr.statusText} <==> ${xhr.readyState}`);
            }else{
                console.log(`Complete connect: ${xhr.status}`);

                setTimeout(() => {
                    location.reload()
                }, 1000);
            }
        }
    })        
}
