

function showpassword(){
let e = document.getElementById("Psw");
let i = document.getElementById("img");
if (e.type == "password") {
  e.type = "text"
  i.src="/static/image/eye-open.png"
} else {
  e.type = "password"
  i.src="/static/image/eye-close.png"

}
}


