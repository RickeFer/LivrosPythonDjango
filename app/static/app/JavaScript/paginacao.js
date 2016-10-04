
function teste()
{
    alert('deu certo!');
}

function HiddenShow(div)
{
    //alert(div);
    var obj = document.getElementById(div);
    obj.style.display = obj.style.display == 'block' ? 'none' : 'block';
}