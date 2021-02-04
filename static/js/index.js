const error_color = "border-red-300"
window.setTimeout("hide();", 5000);

function toggle_nav(selected){
    remove_navs()
    selected.classList.add('border-b-2', 'border-blue-600')
    change_div(selected.id)
    
}
function remove_navs(){
    const navs = ['sign-in', 'sign-up']
    navs.forEach((nav)=>{
        const all_matching_navs = document.querySelectorAll('.'+nav)
        all_matching_navs.forEach((matching_nav)=>{
            matching_nav.classList.remove('border-b-2', 'border-gray-900')
        })
    }) 
}

function change_div(value){
    if (value == "sign-in" || value == "sign-in2"){
        document.getElementById('sign-up-div').classList.add('hidden')
        document.getElementById('sign-in-div').classList.remove('hidden')
    }else if (value == "sign-up"|| value == "sign-up2"){
        document.getElementById('sign-in-div').classList.add('hidden')
        document.getElementById('sign-up-div').classList.remove('hidden')
    }
}

function submit_form(form){
    if (form.id == "sign-up-form"){
        if (validate_sign_up()){
            form.submit()
        }
    }else if (form.id == "sign-in-form"){
        if (validate_sign_in()){
            form.submit()
        }
    }
}

function validate_sign_up(){
    const email = document.getElementById('sign-up-email')
    const password = document.getElementById('sign-up-password')
    const c_password = document.getElementById('sign-up-confirmpassword')

    clear_errors(email)
    clear_errors(password)
    clear_errors(c_password)
    
    with_error = []
    
    if (input_is_empty(email)){
        with_error.push(email)
    }
    if (input_is_empty(password)){
        with_error.push(password)
    }
    if (input_is_empty(c_password)){
        with_error.push(c_password)
    }
    
    if (!match_passwords(password, c_password)){
        with_error.push(password, c_password)
    }

    display_errors(with_error)
    
    if (with_error.length > 0){
        return false
    }else{
        return true
    }
}

function validate_sign_in(){
    const email = document.getElementById('sign-in-email')
    const password = document.getElementById('sign-in-password')

    clear_errors(email)
    clear_errors(password)

    with_error = []
    if (input_is_empty(email)){
        with_error.push(email)
    }
    if (input_is_empty(password)){
        with_error.push(password)
    }

    display_errors(with_error)
    
    if (with_error.length > 0){
        return false
    }else{
        return true
    }
}

function clear_errors(inp){
    inp.classList.remove(error_color)
}

function input_is_empty(inp){
    if (inp.value.length == 0 ){
        return true
    }
    return false
}

function match_passwords(inp1, inp2){
    if (inp1.value != inp2.value){
        return false
    }
    return true
}

function display_errors(errs){
    errs.forEach((err)=>{
        err.classList.add(error_color)
    })
}

function hide(){
document.getElementById("error").classList.add('hidden')
}