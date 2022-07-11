window.oncontextmenu = function(event){
    event.preventDefault()
}

let formSendFile = document.getElementById('formfile')
let sendFileBtn = document.getElementById('send_file_btn')
let chooseFile = document.getElementById('choose_file')
let backToPageBtn = document.getElementById('back_to_page')
let modelMain = document.getElementById('modalmain')
let addModalWindow = document.getElementById('addmodalwindow')
let formResume = document.getElementById('form_correct_data')
let sendResumeBtn = document.getElementById('send_resume_btn')
let logoutUser = document.getElementById('logout')
let nextPageBtn = document.getElementById('nextpage')
let previousPageBtn = document.getElementById('previouspage')

logoutUser.onclick = function(){
    localStorage.removeItem('refresh')
    localStorage.removeItem('access')
    location.href = 'http://localhost:5500'
}

// http://localhost:8000/api/v1/resume/
// http://localhost:8000/api/v1/resume/?page=2

async function getResume(url){
    let token = `Usr ${localStorage.access}`
    let response = await fetch(url, {
        method: 'GET',
        headers: {
            'Authorization':token
        }
    })
    .then(response => response.json())
    .then(data => {
        data.results.forEach(element => {
            document.querySelector('.post').innerHTML += `
            <div class="content">
                <h2>Full name: ${element.full_name}</h2>
                <h3>Email: ${element.email}<h3>
                <h3>Phone: ${element.phone_number}<h3>
                <h3>Skills: ${element.skills}<h3>
            </div>
            `
        });
        pages = {
            'next': data.next,
            'previous': data.previous
        }
        return pages
    })
    .catch(err => {
        console.log(err);
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

formSendFile.onsubmit = async(e) => {
    formResume.reset()
    e.preventDefault();
    let response = await fetch('http://localhost:8000/api/v1/resume/pars/',{
        method: 'POST',
        body: new FormData(formSendFile)
    })
    .then(response => response.json())
    .then(data => {
        modelMain.style.display = 'block'
        addModalWindow.style.display = 'block'
        formResume.full_name.value = data.full_name
        formResume.email.value = data.email
        formResume.phone_number.value = data.phone_number
        formResume.education.value = data.education
        formResume.experience.value = data.experience
        formResume.skills.value = data.skills
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

function mainContent(){
    pages = getResume('http://localhost:8000/api/v1/resume/')
    console.log(pages)
}
mainContent()
