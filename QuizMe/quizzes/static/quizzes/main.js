console.log('Hello World')


const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirms')
const startBtn = document.getElementById('start-button')

const url = window.location.href
modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-quiz')
    const numQuestions = modalBtn.getAttribute('data-question')
    const difficulty = modalBtn.getAttribute('data-difficulty')
    const scoreToPass = modalBtn.getAttribute('data-pass')
    const time = modalBtn.getAttribute('data-time')

    modalBody.innerHTML = '<div class="h5 mb-3">Are you sure you want to begin <b>'+name+'</b>?</div>'+
        '<div class="text-muted"><ul><li>Difficulty : <b>'+difficulty+'</b></li><li>Number of Questions : <b>'+numQuestions+'</b></li><li>Passing Score : <b>'+scoreToPass+'%</b></li><li>Duration : <b>'+time+' mins</b></li></ul></div>';
        startBtn.addEventListener('click',()=>{
            window.location.href = url + pk
        })
    
}))
