window.addEventListener('DOMContentLoaded', function() { 
    
    Show_List()
})
    

function Login(){ // 로그인
    var ID = document.getElementById('Login_ID').value
    var PW = document.getElementById('Login_PW').value

    console.log(ID)
    console.log(PW)

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/Login_DB", true);
    xhr.setRequestHeader('Content-Type', 'application/json'); 
    xhr.send(JSON.stringify({ 

        ID : document.getElementById('Login_ID').value,
        PW : document.getElementById('Login_PW').value

    }));
    xhr.onload = function() {
    
        data = JSON.parse(this.responseText)
        
        if (data == false){
            Swal.fire(
                '로그인에 실패하였습니다.',
                '아이디 또는 비밀번호를가 일치하지 않습니다.',
                'error'
            )
        }else{
            Swal.fire(
                '로그인에 성공하였습니다.',
                'ID : ' + (data[0][0]) + ' Name: ' + (data[0][2]),
                'success'
            )
        }
    }

}

function Sign_in(){ //회원가입

    var ID = document.getElementById('New_ID').value
    var PW = document.getElementById('New_PW').value
    var Name = document.getElementById('New_Name').value
    var Phone = document.getElementById('New_Phone').value

    console.log(ID)
    console.log(PW)
    console.log(Name)
    console.log(Phone)
    
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/Sign_DB", true);
    xhr.setRequestHeader('Content-Type', 'application/json'); 
    xhr.send(JSON.stringify({ 

        ID : document.getElementById('New_ID').value,
        PW : document.getElementById('New_PW').value,
        Name : document.getElementById('New_Name').value,
        Phone : document.getElementById('New_Phone').value

    }));
    xhr.onload = function() {
        data = JSON.parse(this.responseText)
        console.log(data)
    }
}

function Serch_User(){ // 계정찾기

    var Name = document.getElementById('Name').value
    var Phone = document.getElementById('Phone').value

    console.log(Name)
    console.log(Phone)

    var xhr = new XMLHttpRequest()
    xhr.open("POST", "/User_DB", true)
    xhr.setRequestHeader('Content-Type','application/json')
    xhr.send(JSON.stringify({

        Name : document.getElementById('Name').value,
        Phone : document.getElementById('Phone').value

    }))
    xhr.onload = function(){
        var data = JSON.parse(this.responseText)
        console.log("아이디 : ", data[0][0])
        console.log("비밀번호 : ", data[0][1])
    }
    
}

function Notice_Board(){ //게시판 글올리기

    var Title = document.getElementById('Title').value
    var Main_Text = document.getElementById('Main_Text').value

    console.log(Title)
    console.log(Main_Text)

    var xhr = new XMLHttpRequest()
    xhr.open("POST", "/Notice_DB", true)
    xhr.setRequestHeader('Content-Type','application/json')
    xhr.send(JSON.stringify({

        Title : Title,
        Main_Text : Main_Text

    }))
    xhr.onload = function(){
        var data = JSON.parse(this.responseText)
        console.log(data)
    }
}


function Serch_Title(){ // 게시판 찾기

    var Title = document.getElementById('Title_text').value

    console.log(Title)

    var xhr = new XMLHttpRequest()
    xhr.open("POST", "/Title_DB", true)
    xhr.setRequestHeader('Content-Type', 'application/json')
    xhr.send(JSON.stringify({

        Title : document.getElementById('Title_text').value
    }))
    xhr.onload = function(){
        var data = JSON.parse(this.responseText)
        console.log("제목 : ", data[0][0])
        console.log("내용 : ", data[0][1])
    }
}


function Check_Login(){ // 로그인창 새로만들기

    var ID = document.getElementById('ID').value
    var PW = document.getElementById('PW').value

    console.log(ID)
    console.log(PW)

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/Check_Login", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({

        ID : document.getElementById('ID').value,
        PW : document.getElementById('PW').value

    }));
    xhr.onload = function() {
    var data = JSON.parse(this.responseText)
        console.log(data)
        if(ID != data[0][0] && PW != data[0][1]){
            
            alert("비밀번호가 틀렸습니다.")
        }
        else if (ID == data[0][0] && PW == data[0][1]){

            alert("로그인에 성공하였습니다.")
            location.href = "/Test_Page";
        }
    }

}

function Information(){ // 회원정보 등록

    var ID = document.getElementById('ID').value
    var PW = document.getElementById('PW').value
    var Re_PW = document.getElementById('Re_PW').value
    var Name = document.getElementById('Name').value

    console.log(ID)
    console.log(PW)
    console.log(Re_PW)
    console.log(Name)

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/Information", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({

        ID : document.getElementById('ID').value,
        PW : document.getElementById('PW').value,
        Re_PW : document.getElementById('Re_PW').value,
        Name : document.getElementById('Name').value

    }));
    xhr.onload = function() {
    var data = JSON.parse(this.responseText)
    console.log(data);
    alert("회원정보가 등록되었습니다.")
    }

}

function Ch_information(){ // 개인정보 수정

    var Ch_PW = document.getElementById('Ch_PW').value
    var Ch_RePW = document.getElementById('Ch_RePW').value

    console.log(Ch_PW)
    console.log(Ch_RePW)

    var xhr = new XMLHttpRequest()
    xhr.open("POST", "/Ch_information", true)
    xhr.setRequestHeader('Content-Type', 'application/json')
    xhr.send(JSON.stringify({

        Ch_PW : document.getElementById('Ch_PW').value,
        Ch_RePW : document.getElementById('Ch_RePW').value
    }))
    xhr.onload = function(){
        var data = JSON.parse(this.responseText)
        alert("개인정보가 수정되었습니다. 다시 로그인해주세요")
        location.href ='/'
    }
}

function Upload_Notice(){

    var Notice_Title = document.getElementById('Notice_Title').value
    var Notice = document.getElementById('Notice').value

    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    var yyyy = today.getFullYear();

    today = yyyy+ '.' + mm + '.' + dd ;

    console.log(Notice_Title)
    console.log(Notice)
    console.log(today)

    var xhr = new XMLHttpRequest()
    xhr.open("POST","/Upload_Notice", true)
    xhr.setRequestHeader('Content-Type', 'application/json')
    xhr.send(JSON.stringify({

        Notice_Title : document.getElementById('Notice_Title').value,
        Notice : document.getElementById('Notice').value,
        today : today
    }))
    xhr.onload = function(){
        var data = JSON.parse(this.responseText)

        
        alert("작성글이 올라갔습니다."+today+"")
        location.href ='/Test_Page'
    }
}


function Show_List(){ // 파이썬에서 세션값 받아오기
    // console.log("Show_List")
    // // var UserID = document.getElementsByTagName(session['User_ID']).value
    // console.log(sessionStorage.getItem('User_ID'))
    // // var data = document.getElementById()
    // // console.log(data)

    // //   var test_ID = sessionStorage.getItem("User_ID")
    // var test_ID = FormData("User_ID").value
    // // var test_ID = session['User_ID'].value
    // alert("팝업창 테스트")
    // console.log(test_ID)



    
    var xhr = new XMLHttpRequest()
    xhr.open("POST","/Return_Session", true)
    xhr.setRequestHeader('Content-Type', 'application/json')
    xhr.send(JSON.stringify({
        
        data : 1 // POST로 보낼 신호(아무거나)
    }))
    xhr.onload = function(){
        var data = JSON.parse(this.responseText)
        data = JSON.parse(this.responseText)
        // document.getElementById('Title').innerText=data
        document.getElementById('Title1').innerText=JSON.parse(data)[0][2]
        document.getElementById('date1').innerText=JSON.parse(data)[0][4]
        document.getElementById('View1').innerText=JSON.parse(data)[0][5]
    
        document.getElementById('Title2').innerText=JSON.parse(data)[1][2]
        document.getElementById('date2').innerText=JSON.parse(data)[1][4]
        document.getElementById('View2').innerText=JSON.parse(data)[1][5]

        document.getElementById('Title3').innerText=JSON.parse(data)[2][2]
        document.getElementById('date3').innerText=JSON.parse(data)[2][4]
        document.getElementById('View3').innerText=JSON.parse(data)[2][5]
        
        document.getElementById('Title4').innerText=JSON.parse(data)[3][2]
        document.getElementById('date4').innerText=JSON.parse(data)[3][4]
        document.getElementById('View4').innerText=JSON.parse(data)[3][5]
        
        document.getElementById('Title5').innerText=JSON.parse(data)[4][2]
        document.getElementById('date5').innerText=JSON.parse(data)[4][4]
        document.getElementById('View5').innerText=JSON.parse(data)[4][5]

        document.getElementById('Title6').innerText=JSON.parse(data)[5][2]
        document.getElementById('date6').innerText=JSON.parse(data)[5][4]
        document.getElementById('View6').innerText=JSON.parse(data)[5][5]
        
        document.getElementById('Title7').innerText=JSON.parse(data)[6][2]
        document.getElementById('date7').innerText=JSON.parse(data)[6][4]
        document.getElementById('View7').innerText=JSON.parse(data)[6][5]

        document.getElementById('Title8').innerText=JSON.parse(data)[7][2]
        document.getElementById('date8').innerText=JSON.parse(data)[7][4]
        document.getElementById('View8').innerText=JSON.parse(data)[7][5]
        
        document.getElementById('Title9').innerText=JSON.parse(data)[8][2]
        document.getElementById('date9').innerText=JSON.parse(data)[8][4]
        document.getElementById('View9').innerText=JSON.parse(data)[8][5]
        
        document.getElementById('Title10').innerText=JSON.parse(data)[9][2]
        document.getElementById('date10').innerText=JSON.parse(data)[9][4]
        document.getElementById('View10').innerText=JSON.parse(data)[9][5]

        console.log(JSON.parse(data))
    }

}


function Main_Text1(){ //게시글 정보 띄우기


    Title = document.getElementById('Title1').innerText

    var xhr = new XMLHttpRequest()
    xhr.open("POST","/Read_Text",true)
    xhr.setRequestHeader('Content-Type','application/json')
    xhr.send(JSON.stringify({

        Title : document.getElementById('Title1').innerText,
        View : 1
    }))
    xhr.onload = function(){
        var data = JSON.parse(this.responseText)
        Swal.fire(
            (data[0][2]),
            (data[0][3]),
            'success'
        )
        document.getElementById('View1').innerText=data[0][5]
    }
}
function Main_Text2(){ //게시글 정보 띄우기

    Title = document.getElementById('Title2').innerText

    var xhr = new XMLHttpRequest()
    xhr.open("POST","/Read_Text",true)
    xhr.setRequestHeader('Content-Type','application/json')
    xhr.send(JSON.stringify({

        Title : document.getElementById('Title2').innerText,
        View : 1
    }))
    xhr.onload = function(){
        var data = JSON.parse(this.responseText)
        Swal.fire(
            (data[0][2]),
            (data[0][3]),
            'success'
        )
        document.getElementById('View2').innerText=data[0][5]
    }
}
function Main_Text3(){ //게시글 정보 띄우기

    Title = document.getElementById('Title3').innerText

    var xhr = new XMLHttpRequest()
    xhr.open("POST","/Read_Text",true)
    xhr.setRequestHeader('Content-Type','application/json')
    xhr.send(JSON.stringify({

        Title : document.getElementById('Title3').innerText,
        View : 1
    }))
    xhr.onload = function(){
        var data = JSON.parse(this.responseText)
        Swal.fire(
            (data[0][2]),
            (data[0][3]),
            'success'
        )
        document.getElementById('View3').innerText=data[0][5]
    }
}
function Main_Text4(){ //게시글 정보 띄우기

    Title = document.getElementById('Title4').innerText

    var xhr = new XMLHttpRequest()
    xhr.open("POST","/Read_Text",true)
    xhr.setRequestHeader('Content-Type','application/json')
    xhr.send(JSON.stringify({

        Title : document.getElementById('Title4').innerText,
        View : 1
    }))
    xhr.onload = function(){
        var data = JSON.parse(this.responseText)
        Swal.fire(
            (data[0][2]),
            (data[0][3]),
            'success'
        )
        document.getElementById('View4').innerText=data[0][5]
    }
}
function Main_Text5(){ //게시글 정보 띄우기

    Title = document.getElementById('Title5').innerText

    var xhr = new XMLHttpRequest()
    xhr.open("POST","/Read_Text",true)
    xhr.setRequestHeader('Content-Type','application/json')
    xhr.send(JSON.stringify({

        Title : document.getElementById('Title5').innerText,
        View : 1
    }))
    xhr.onload = function(){
        var data = JSON.parse(this.responseText)
        Swal.fire(
            (data[0][2]),
            (data[0][3]),
            'success'
        )
        document.getElementById('View5').innerText=data[0][5]
    }
}
function Main_Text6(){ //게시글 정보 띄우기

    Title = document.getElementById('Title6').innerText

    var xhr = new XMLHttpRequest()
    xhr.open("POST","/Read_Text",true)
    xhr.setRequestHeader('Content-Type','application/json')
    xhr.send(JSON.stringify({

        Title : document.getElementById('Title6').innerText,
        View : 1
    }))
    xhr.onload = function(){
        var data = JSON.parse(this.responseText)
        Swal.fire(
            (data[0][2]),
            (data[0][3]),
            'success'
        )
        document.getElementById('View6').innerText=data[0][5]
    }
}
function Main_Text7(){ //게시글 정보 띄우기

    Title = document.getElementById('Title7').innerText

    var xhr = new XMLHttpRequest()
    xhr.open("POST","/Read_Text",true)
    xhr.setRequestHeader('Content-Type','application/json')
    xhr.send(JSON.stringify({

        Title : document.getElementById('Title7').innerText,
        View : 1
    }))
    xhr.onload = function(){
        var data = JSON.parse(this.responseText)
        Swal.fire(
            (data[0][2]),
            (data[0][3]),
            'success'
        )
        document.getElementById('View7').innerText=data[0][5]
    }
}
function Main_Text8(){ //게시글 정보 띄우기

    Title = document.getElementById('Title8').innerText

    var xhr = new XMLHttpRequest()
    xhr.open("POST","/Read_Text",true)
    xhr.setRequestHeader('Content-Type','application/json')
    xhr.send(JSON.stringify({

        Title : document.getElementById('Title8').innerText,
        View : 1
    }))
    xhr.onload = function(){
        var data = JSON.parse(this.responseText)
        Swal.fire(
            (data[0][2]),
            (data[0][3]),
            'success'
        )
        document.getElementById('View8').innerText=data[0][5]
    }
}
function Main_Text9(){ //게시글 정보 띄우기

    Title = document.getElementById('Title9').innerText

    var xhr = new XMLHttpRequest()
    xhr.open("POST","/Read_Text",true)
    xhr.setRequestHeader('Content-Type','application/json')
    xhr.send(JSON.stringify({

        Title : document.getElementById('Title9').innerText,
        View : 1
    }))
    xhr.onload = function(){
        var data = JSON.parse(this.responseText)
        Swal.fire(
            (data[0][2]),
            (data[0][3]),
            'success'
        )
        document.getElementById('View9').innerText=data[0][5]
    }
}
function Main_Text10(){ //게시글 정보 띄우기

    Title = document.getElementById('Title10').innerText

    var xhr = new XMLHttpRequest()
    xhr.open("POST","/Read_Text",true)
    xhr.setRequestHeader('Content-Type','application/json')
    xhr.send(JSON.stringify({

        Title : document.getElementById('Title10').innerText,
        View : 1
    }))
    xhr.onload = function(){
        var data = JSON.parse(this.responseText)
        Swal.fire(
            (data[0][2]),
            (data[0][3]),
            'success'
        )
        document.getElementById('View10').innerText=data[0][5]
    }
}

function User_Name(User_Name){

    var Name = User_Name

    console.log(Name)
}

function Add_List(){ // 테이블 행 추가(수동적)

    const table = document.getElementById('User_Info')
    // 행 추가
    const New_List = table.insertRow()
    // 행에 cell 추가
    const NewCell_1 = New_List.insertCell(0)
    const NewCell_2 = New_List.insertCell(1)
    // cell에 텍스트 추가
    NewCell_1.innerText = '제목'
    NewCell_1.innerText = '내용'


}


function test_Check(User_Name){

	var today = new Date();
	var dd = String(today.getDate()).padStart(2, '0');
	var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
	var yyyy = today.getFullYear();

	today = yyyy+ '.' + mm + '.' + dd ;
    document.getElementById('Title1').innerText=JSON.parse(data)[0][2]
	
	console.log("오늘은 "+today+" 입니다");
}