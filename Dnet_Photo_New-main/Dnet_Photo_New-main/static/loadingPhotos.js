window.addEventListener('DOMContentLoaded', function() { 
    
})


function search(){
    console.log("search")
    var location = document.getElementById('location').value
    var startdate = document.getElementById('startdate').value
    var enddate = document.getElementById('enddate').value
    var lim = document.getElementById('lim').value

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/searchDB", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        location: location,
        startdate : startdate,
        enddate : enddate,
        lim : lim
    }));
    xhr.onload = function() {
    var data = JSON.parse(this.responseText)
    console.log(data[1]);
    document.getElementById('inst').innerHTML += ('<tr><td>일시</td><td>속도</td><td>사진보기</td></tr>');
    for(i in data){
        console.log(i)
        document.getElementById('inst').innerHTML += ('<tr><td>'+data[i][2]+'</td><td>'+data[i][1]+'Km/h'+'</td><td> <button onClick="photo(this.id)" class="buletxt" style="cursor:pointer;" id="'+data[i][3]+'"</td>OPEN</tr>');
            
    }

}

}

function photo(s){

    document.getElementById(s).style.backgroundColor='rgba(0, 0, 0, 0.5)'
    if(btn != 0){
    document.getElementById(btn).style.backgroundColor='rgb(255, 255, 255)'
    }
    btn = s

    document.getElementById('image').src = s.replace('"',"").replace("/home/pi/Desktop/Dnet_Photo_New","")
    document.all.btn.style.display="";

    document.all.btn.innerHTML = "<a id='down' href='/static/logo2.png' download> <button id='led_on' class='btn1' onclick='download_click(this.id);'>Download</button></a>  "
    // <button id='led_on2' class='btn1' onclick='remove_click(this.id);'>REMOVE</button>
    var changeid12 = document.getElementById("down"); 
    changeid12.setAttribute("href",s.replace('"',"").replace("/home/pi/Desktop/Dnet_Photo_New",""))  
    changeid12.setAttribute("id",s.replace('"',"").replace("/home/pi/Desktop/Dnet_Photo_New",""))  

    var changeid12 = document.getElementById("led_on2"); 
    changeid12.setAttribute("id",s)  
}

function excel(){
    var location = document.getElementById('location').value
    var startdate = document.getElementById('startdate').value
    var enddate = document.getElementById('enddate').value
    var lim = document.getElementById('lim').value

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/excelexport", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        location: location,
        startdate : startdate,
        enddate : enddate,
        lim : lim
    }));
    Swal.fire({
        title: '엑셀 파일 생성중',
        showConfirmButton: false,
        allowOutsideClick: false,
        allowEscapeKey: false
      })
    xhr.onload = function() {
        Swal.fire({
            title: '<strong><b>엑셀 파일 생성 완료!</b></strong>',
            icon: 'success',
            html:
             
              '<a href="/static/exli.xlsx">여기</a>' +
              '를 클릭하여 엑셀 파일을 다운받을수 있습니다',
            focusConfirm: false,
            confirmButtonText:
              '<i class="fa fa-thumbs-up"></i> 닫기',
            confirmButtonAriaLabel: 'Thumbs up, great!',
            showCancelButton: false
          })
    console.log("OK");

}
}