
function Ch_Number(){

    var num = document.getElementById('CarNumber').value

    console.log(num)

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/Ch_Number", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({

        num : CarNumber
    }));
    xhr.onload = function() {
    var data = JSON.parse(this.responseText)

        console.log(data);
        alert(data)
    }
}
