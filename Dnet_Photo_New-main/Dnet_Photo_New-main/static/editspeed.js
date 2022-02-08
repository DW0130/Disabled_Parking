var idd

    
    var e = document.getElementById("location");
    var idd
    async function editspeedli() {
        
        var e = document.getElementById("location");
    
    
        const { value: select } = await Swal.fire({
            title: '장소 선택',
            input: 'select',
            inputOptions: {
    
                A: '센서 1',
                B: '센서 2',
                C: '센서 3',
                D: '센서 4',
                E: '센서 5',
                F: '센서 6'
              
            },
            inputValue: e.options[e.selectedIndex].id,
            showCancelButton: true,
    
          })
          
          if (select) {
            idd = select
            var win = window.open("", "a", "width=1200, height=800, left=100, top=50");
            win.document.write("<p>속도값 변경</p>");
    
            win.document.write('<button type="button" onclick="popup()">속도 데이터 변경</button>');
            win.document.write('<script type="text/javascript" src="/static/editspeed.js"></script>');
            win.document.write('<link href="{{ url_for("static", filename="popup.css") }}" rel="stylesheet"></link>');




            var rawFile= new XMLHttpRequest();
                rawFile.open("GET", "/static/speeddata/speedlimit_"+idd+".txt"+"?"+(new Date()).getTime(), false);
                rawFile.onreadystatechange= function ()
                {
                
                            var allText= rawFile.responseText;
                            //alert(allText);
                            win.document.write('<br><textarea type="text" id="tex" class="inputbox" style="width:800px;height:650px;font-size:30px;">'+allText+'</textarea>');
                            console.log(allText)
                    
                }
                rawFile.send(null);

                var form = document.createElement('form');
            form.setAttribute('method', 'post');
            form.setAttribute('action', '/idd');
            document.charset = "utf-8";
            //console.log(a)
            var hiddenField = document.createElement('input');
            hiddenField.setAttribute('type', 'hidden');
            hiddenField.setAttribute('name', 'id');
            hiddenField.setAttribute('value', idd);
            form.appendChild(hiddenField);
            document.body.appendChild(form);
            form.submit();


            console.log(idd)
    }
}


function popup(){
    var textarea = document.getElementById('tex');
    var edtxt = textarea.value
   //saveStrings(edtxt, '/static/speeddata/add.txt');
   //var xhr = new XMLHttpRequest();
   //xhr.open( 'post', "/static/speeddata/speedlimit_A.txt", true );
   //xhr.send(edtxt);
   var form = document.createElement('form');
   form.setAttribute('method', 'post');
   form.setAttribute('action', '/edit');
   document.charset = "utf-8";
   //console.log(a)
   var hiddenField = document.createElement('input');
   hiddenField.setAttribute('type', 'hidden');
   hiddenField.setAttribute('name', 'ed');
   hiddenField.setAttribute('value', edtxt);
   form.appendChild(hiddenField);
   document.body.appendChild(form);
   form.submit();
   //console.log(a)
    console.log(edtxt);
    //console.log("asdasdasd")
    alert("저장되었습니다");
}

