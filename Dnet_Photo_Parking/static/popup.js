        
var inter = setInterval(  
     
        async () => { 
        var request = new XMLHttpRequest();
        //console.log(state);
        
        console.log("req");
        
        request.open('GET', '/dbscrch2');
        
        request.responseType = 'json';
        request.send();
        
        request.onload = function() {


                var myJson = request.response;
                let a = JSON.stringify(myJson.aa);
                let date = JSON.stringify(myJson.dete);
                let plate = JSON.stringify(myJson.plate);
                let speed = JSON.stringify(myJson.speed);
                let fi = JSON.stringify(myJson.file)
                if (a == -5){
                        //alert("3회 누적 감지.");
                        clearInterval(inter); 
                }else{
                console.log(myJson)
                let items = [
                        'Blue',
                        'Red',
                        'White',
                        'Green',
                        'Black',
                        'Orange'
                    ],
                    ul = document.createElement('ul');

                document.getElementById('bus').appendChild(ul);
                document.getElementById('plate').innerText=plate.replace('"',"")

                console.log(plate)
                let li = document.createElement('li');
                ul.appendChild(li);
                fi = fi.replace('"',"").replace("/home/pi/Desktop/Dnet_WEB_/Dnet_Photo-management/Web_server2","").replace('g"',"g")

                //li.innerHTML += JSON.stringify(item);
                li.innerHTML += ("<button type='button' class='button' name='locat' onclick='loadbus(this.id)'value=" + date+"id="+ fi+">"+ date.replace('"',"").replace('"',"")+"   "+speed+"km");
        
                }
        }
}
,100
)

function loadbus(s){ 


        document.getElementById('image').src = s
        

       


    }