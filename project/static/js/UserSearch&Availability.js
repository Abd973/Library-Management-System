
function search() {
    let filter = document.getElementById('bsearch').value.toUpperCase();
    let item = document.querySelectorAll('.book');
    let l = document.getElementsByTagName('h3');
    for(var i = 0;i<=l.length;i++){
    let a=item[i].getElementsByTagName('h3')[0];
    let value=a.innerHTML || a.innerText || a.textContent;
    if(value.toUpperCase().indexOf(filter) > -1) {
    item[i].style.display="inline-block";
    }
    else
    {
    item[i].style.display="none";
    }
    }
    }
   
    function Availability(button) {
        var statusParagraph = button.previousElementSibling;
        statusParagraph.textContent = "Unavailable";
    
        button.textContent = "Borrowed";
    
        button.disabled = true;
    }
