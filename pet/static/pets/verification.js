document.addEventListener('DOMContentLoaded',()=>{
    verificate()
})



function verificate(){
    const email= document.querySelector('#inputEmail');
    const name=document.querySelector('#name');
    const password=document.querySelector('#password');
    const password2=document.querySelector('#password2');
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    name.addEventListener('blur',()=>{
         if (name.value==''){
            name.classList.add('border','border-danger')
            }else{
            name.classList.remove('border','border-danger')
            }
    })
    password.addEventListener('blur',()=>{
        if (password.value=='' || password.value.length<8){
            password.classList.add('border','border-danger')
        }else{
            password.classList.remove('border','border-danger')
        }
    })
    password2.addEventListener('blur',()=>{
        if (password2.value==''){
            password2.classList.add('border','border-danger')
        }else{
            password2.classList.remove('border','border-danger')
        }
    })

    email.addEventListener('blur',()=>{
       if (email.value=='' || !emailRegex.test(email.value)){
              email.classList.add('border','border-danger')
       }else{
              email.classList.remove('border','border-danger')
       }

    })

    inputs=document.querySelectorAll('input').foreach(n=>{
        if (n.value==''){
           console.log(document.querySelector('#submitForm')); 
        }
    })
}

