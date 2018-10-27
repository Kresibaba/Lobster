document.getElementById('id_username').placeholder = "Enter your username";
document.getElementById('id_password').placeholder = "Enter your password";

login_btn = document.getElementById('login_but');

function login_btn_normal () {
    login_btn.style.border = "solid grey 1px";
    login_btn.style.borderRadius = "4px";
    login_btn.style.textDecoration = "None";
    login_btn.style.color = "grey";
    login_btn.style.height = "100%";
    login_btn.style.width = "50%";
    login_btn.style.textAlign = "center";
    login_btn.style.overflow = "auto";
    login_btn.style.font = "bold 16px Helvetica sans-serif";
    login_btn.style.backgroundColor = "rgba(1,1,1,0)";
}

function login_btn_hover () {
    login_btn.style.border = "solid black 1px";
    login_btn.style.color = "black";
}