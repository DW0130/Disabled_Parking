#This is a python
from atexit import register
from cgi import test
from cgitb import html
from dataclasses import dataclass
from email.mime import application
import re
from shutil import which
#from crypt import methods
from tokenize import Name
from turtle import update
from unittest import result
from webbrowser import get
from flask import Flask,render_template,request,send_file,redirect,session,flash, url_for
from pymysql import NULL

from werkzeug.utils import secure_filename # 리눅스서버사용 : from werkzeug, 윈도우서버사용 : from werkzeug.utils 
import os,sys
import time
import hashlib
import pymysql
import threading
import openpyxl
import statistics
from openpyxl import Workbook, drawing 


DELETE = "rm -f /home/pi/Desktop/Dnet_WEB_/Dnet_Photo-management/Web_server2"
str2 = '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'

import json

app = Flask(__name__,template_folder='templates')
app.secret_key = 'asdf'
app.config["SECRET_KEY"] = "ABCD"




def shutdown_server():
    
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


# 화면 슬라이스 생성
@app.route("/") # 프로그램 시작시 먼저 실행
def main():
    return render_template('test_excel.html')
    
@app.route("/Test_Page") # 프로그램 시작시 먼저 실행
def Test_Page():
    if(session.get('login_ss')):
        return render_template('Test_Page.html')
    else:
        flash("로그인이 필요합니다.")
        return redirect('/')
    
@app.route("/List_Page") # 프로그램 시작시 먼저 실행
def List_Page():
    if(session.get('login_ss')):    
        return render_template('List_Page.html')
    else:
        return redirect('/')
    
@app.route("/Notice_Board") # 프로그램 시작시 먼저 실행
def Notice_Board():
    if(session.get('login_ss')):
        return render_template('Notice_Board.html')
    else:
        return redirect('/')




'''
@app.route("/") # 프로그램 시작시 먼저 실행
def main():
    return render_template('test_login.html')

@app.route("/test_Sign") # 회원가입
def test_Sign():
    return render_template('test_Sign.html')
    
@app.route("/test_Serch_User") # 계정찾기
def test_Serch_User():
    return render_template('test_Serch_User.html')

@app.route("/test_writing") # 계정찾기
def test_writing():
    return render_template('test_writing.html')
'''

'''
@app.route("/") # 프로그램 시작시 먼저 실행
def main():
    return render_template('login_Before.html')

@app.route("/sign_up") #회원가입화면
def sign_up():
    return render_template('sign_up.html')

@app.route("/login_Before") #메인화면
def login_Before():
    return render_template('login_Before.html')

@app.route("/Serch_ID") #ID찾기
def Serch_ID():
    return render_template('Serch_ID.html')

@app.route("/Serch_PW") #PW찾기
def Serch_PW():
    return render_template('Serch_PW.html')

@app.route("/blog") #blog화면
def blog():
    return render_template('blog.html')
    
@app.route("/login_after") #blog화면
def login_after():
    return render_template('login_after.html')
'''

'''
@app.route("/popup")
def popup():
    return render_template('popup.html')

@app.route("/idd",methods=['POST'])
def idd():
    id=""
    if request.method == 'POST':
        id = request.form.get('id')
   
    session['iddd'] = id
    return ('', 204)

@app.route("/edit",methods=['POST'])
def editspeed():
    ed=""
    if request.method == 'POST':
        ed = request.form.get('ed')
    print(ed)
    fn = session['iddd']
    print(fn)
    f = open("/home/pi/Desktop/Dnet_Photo_New/static/speeddata/speedlimit_"+fn+".txt", 'w')   
    f.write(ed)
    f.close()
    return ('', 204)

@app.route("/list")
def listmain():
    if (session.get('login')) :
        return render_template('listmain.html')
    else :
        flash("로그인이 필요합니다")
        return redirect('/')

@app.route("/analysis")
def analysis():
    if (session.get('login')) :
        return render_template('analysis.html')
    else :
        flash("로그인이 필요합니다")
        return redirect('/')

@app.route("/p2",methods=['POST'])
def realmain():
    num=""
    num2=""
    if request.method == 'POST':
        num = request.form.get('num')
        num2 = request.form.get('num2')
        result = hashlib.sha256(num2.encode()).hexdigest()
        if (num == "dnet" and num2 == "admin") or (num =='a' and result == str2):
            session['login'] = 1
            return redirect('/list')
        else:
            flash("아이디 또는 비밀번호가 일치하지 않습니다")
            return render_template('login.html')

@app.route("/re",methods=['POST'])
def remove():
    if request.method == 'POST':
        a = request.form.get('url')
        DELETE_ORDER = DELETE + a
        print(DELETE_ORDER)
        os.system(DELETE_ORDER)
    return redirect('/list')

@app.route("/searchDB",methods=['POST'])
def searchDB():
    if request.method == 'POST':
        i = request.get_json()
        
        DB = pymysql.connect(host='192.168.0.43',user='root',password='1234',db='speeddb',charset='utf8')  
        sql = DB.cursor()
        sql.execute("select LCT,SPD,TME,PHT from speeddb.CarDB where TME between '"+i.get('startdate')+"' and '"+i.get('enddate')+"' AND SPD >"+i.get('lim')+" AND LCT ='"+i.get('location')+"' ORDER BY TME DESC")
        data = json.dumps(sql.fetchall(),default=str)
        return data

@app.route("/searchDBAn",methods=['POST'])
def searchDBAn():
    if request.method == 'POST':
        i = request.get_json()
        
        DB = pymysql.connect(host='192.168.0.43',user='root',password='1234',db='speeddb',charset='utf8')  
        sql = DB.cursor()
        sql.execute("select LCT,SPD,HOUR(TME) from speeddb.CarDB where TME between '"+i.get('startdate')+"' and '"+i.get('enddate')+"' AND SPD >"+i.get('lim')+" ORDER BY TME DESC")
        data = json.dumps(sql.fetchall(),default=str)
        return data

@app.route("/excelexport",methods=['POST'])
def excelexport():
    if request.method == 'POST':
        i = request.get_json()
        

        DB = pymysql.connect(host='192.168.0.43',user='root',password='1234',db='speeddb',charset='utf8')  
        try:
            with DB.cursor() as curs:
                sql = "select SPD,TME from speeddb.CarDB where TME between '"+i.get('startdate')+"' and '"+i.get('enddate')+"' AND SPD >"+i.get('lim')+" AND LCT ='"+i.get('location')+"' ORDER BY TME DESC"

                sql2 = "select PHT from speeddb.CarDB where TME between '"+i.get('startdate')+"' and '"+i.get('enddate')+"' AND SPD >"+i.get('lim')+" AND LCT ='"+i.get('location')+"' ORDER BY TME DESC"

                curs2 = DB.cursor()

                curs.execute(sql)
                curs2.execute(sql2)
                rs = curs.fetchall()
                rs2 = curs2.fetchall()

                wb = Workbook()
                ws = wb.active

                #첫행 입력
                ws.append(('번호','이름','d','d'))

                #DB 모든 데이터 엑셀로
                index = 2
                for row in rs:
                    ws.append(row)
                    data4 = rs2[index-2][0]
                    img = openpyxl.drawing.image.Image(data4)
                    img.height = 305.5
                    img.width= 405.5
                    a = 'D'+str(index)
                    ws.add_image(img,a)
                    print("index")
                    print(a)
                    index = index+1
                wb.save("/home/pi/Desktop/Dnet_Photo_New/static/exli.xlsx")
        finally:
            DB.close()
            wb.close()
        return '', 204
'''

'''
@app.route("/testpost",methods=['POST'])
def testpost(): #연습용Post
    Realid = 1234
    Realpw = 5678
    if request.method == 'POST':
        i = request.get_json()
        recvdata = i.get('numder')
        Realid = i.get('ID')
        Realpw = i.get('PW')

        if Realid == '1234' and Realpw == '5678':
            return json.dumps("{'data' : 로그인 되었습니다.}")
        else:
            return json.dumps("{'data' : 비닐번호가 틀렸습니다.}")
       
newid = ''
newpw = ''
@app.route("/Signup_post",methods=['POST']) #회원가입POST
def Signup_post(): #연습용Post
    global newid
    global newpw

    if request.method == 'POST':
        i = request.get_json()
        newid = i.get('New_ID')
        newpw = i.get('New_PW')
        newname = i.get('New_NAME')
        newphone = i.get('New_Phone')
        DB = pymysql.connect(host='192.168.0.43',user='root',password='1234',db='test',charset='utf8')  
        cur = DB.cursor()
        sql = "INSERT IGNORE INTO test.testtable (name,phone,id,pw)  VALUES (%s, %s, %s, %s)"

        val = (newid,newpw,newname,newphone)

        cur.execute(sql, val)
        DB.commit()
        return json.dumps ("{'data' : '회원가입이 되었습니다.'}")


@app.route("/Signup_post_1",methods=['POST']) #회원가입POST
def Signup_post_1(): #연습용Post
    global newid
    global newpw

    if request.method == 'POST': # POST방식으로 요구
        i = request.get_json() # json타입으로 정보가져와 i에 대입
        newid = i.get('New_ID')
        newpw = i.get('New_PW')
        newname = i.get('New_NAME')
        newphone = i.get('New_Phone')
        DB = pymysql.connect(host='192.168.0.43',user='root',password='1234',db='test_naver',charset='utf8')  
        cur = DB.cursor()
        sql = "INSERT IGNORE INTO test_naver.test_table_naver (ID,PW,Name,Phone)  VALUES (%s, %s, %s, %s)"

        val = (newid,newpw,newname,newphone)

        cur.execute(sql, val)
        DB.commit()
        return json.dumps ("{'data' : 'test_회원가입이 되었습니다.'}")


@app.route("/testpost_1",methods=['POST']) #NAVER로그인POST
def testpost_1(): #연습용Post
    global newid
    global newpw
    if request.method == 'POST':
        i = request.get_json()

        if newid == i.get('ID') and newpw == i.get('PW'):
            return json.dumps("{'data' : 로그인 되었습니다.}")
        else:
            return json.dumps("{'data' : 비밀번호가 틀렸습니다.}")


@app.route("/dbsearch",methods=['POST'])
def dbsearch():
    if request.method == 'POST':
        i = request.get_json()
        idd = i.get('ID') #a
        pw = i.get('PW') #a2
        DB = pymysql.connect(host='192.168.0.43',user='root',password='1234',db='test',charset='utf8')  
        sql = DB.cursor()
        sql.execute("select * from test.testtable where id='"+idd+"' and pw='"+pw+"'")
        data = json.dumps(sql.fetchall(),default=str)
        return data
# select * from  test.testtable where id= 'a' and pw='a2'


@app.route("/dbsearch_1",methods=['POST'])
def dbsearch_1():

    if request.method == 'POST':
        i = request.get_json()
        sql_ID = i.get('ID') #a
        sql_PW = i.get('PW') #a2
        DB = pymysql.connect(host='192.168.0.43',user='root',password='1234',db='test_naver',charset='utf8')  
        sql = DB.cursor()
        sql.execute("select * from test_naver.test_table_naver where ID='"+sql_ID+"' and PW='"+sql_PW+"'")
        data = json.dumps(sql.fetchall(),default=str)
        return data
        

        
@app.route("/Serch_User",methods=['POST'])
def Serch_User():
    if request.method == 'POST':
        i = request.get_json()
        sql_Phone = i.get('Serch_Phone')

        DB = pymysql.connect(host='192.168.0.43',user='root',password='1234',db='test_naver',charset='utf8')  
        sql = DB.cursor()
        sql.execute("select * from test_naver.test_table_naver where Phone='"+sql_Phone+"'")
        data = json.dumps(sql.fetchall(),default=str)
        return data



@app.route("/text_Update",methods=['POST']) #블로그 글 업로드
def text_Update():
    global Title
    global Notice

    if request.method == 'POST': # POST방식으로 요구
        i = request.get_json() # json타입으로 정보가져와 i에 대입
        Title = i.get('Title')
        Notice = i.get('Contents')
        DB = pymysql.connect(host='192.168.0.43',user='root',password='1234',db='test_naver',charset='utf8')  
        cur = DB.cursor()
        sql = "INSERT IGNORE INTO test_naver.test_table_blog (Title, Notice)  VALUES (%s, %s)"

        val = (Title, Notice)

        cur.execute(sql, val)
        DB.commit()
        return json.dumps ("{'data' : '게시글이 올라갔습니다.'}")


@app.route("/Serch_Title",methods=['POST']) # 블로그 제목 찾기
def Serch_Title():
    if request.method == 'POST':
        i = request.get_json()
        sql_Title = i.get('ST')

        DB = pymysql.connect(host='192.168.0.43',user='root',password='1234',db='test_naver',charset='utf8')  
        sql = DB.cursor()
        sql_1 = DB.cursor()
        sql.execute("select * from test_naver.test_table_blog where Title='"+sql_Title+"'")
        sql.execute("SELECT * FROM test_table_blog WHERE Title LIKE'%"+sql_Title+"%'") # 특정단어 검색용도이나 도저히 사용 못하겠음
        data = json.dumps(sql.fetchall(),default=str)
        return data
'''
'''
@app.route("/Login_DB",methods=['POST']) # 로그인
def Login_DB():
    if request.method == 'POST': # POST방식으로 들어온 데이터가 있다면 다음과 같이 실행하라
        i = request.get_json()
        UserID = i.get('ID')
        UserPW = i.get('PW')

        DB = pymysql.connect(host='192.168.0.28',user='root',password='1234',db='DW_test',charset='utf8')  
        sql = DB.cursor()
        sql.execute("select * from DW_test.test where ID='"+UserID+"' and PW='"+UserPW+"'")
        data = json.dumps(sql.fetchall(),default=str)
        return data


@app.route("/Sign_DB",methods=['POST']) # 회원가입
def Sign_DB(): #연습용Post

    if request.method == 'POST': # POST방식으로 요구
        i = request.get_json() # json타입으로 정보가져와 i에 대입
        New_ID = i.get('ID')
        New_PW = i.get('PW')
        New_Name = i.get('Name')
        New_Phone = i.get('Phone')
        DB = pymysql.connect(host='192.168.0.28',user='root',password='1234',db='DW_test',charset='utf8')  
        cur = DB.cursor()
        sql = "INSERT IGNORE INTO DW_test.test (ID,PW,Name,Phone)  VALUES (%s, %s, %s, %s)"

        val = (New_ID, New_PW, New_Name, New_Phone)

        cur.execute(sql, val)
        DB.commit()
        return json.dumps ("{'회원가입이 되었습니다.'}")


@app.route("/User_DB",methods=['POST']) # 계정찾기
def User_DB():
    if request.method == 'POST':
        i = request.get_json()
        Name = i.get('Name')
        Phone = i.get('Phone')

        DB = pymysql.connect(host='192.168.0.28',user='root',password='1234',db='DW_test',charset='utf8')  
        sql = DB.cursor()
        sql.execute("select * from DW_test.test where Name='"+Name+"' and Phone='"+Phone+"'")
        data = json.dumps(sql.fetchall(),default=str)
        return data


@app.route("/Notice_DB",methods=['POST']) # 글 업로드
def Notice_DB():

    if request.method == 'POST': # POST방식으로 요구
        i = request.get_json() # json타입으로 정보가져와 i에 대입
        Title = i.get('Title')
        Notice = i.get('Main_Text')
        print(Notice)
        DB = pymysql.connect(host='192.168.0.28',user='root',password='1234',db='DW_test',charset='utf8')  
        cur = DB.cursor()
        sql = "INSERT IGNORE INTO DW_test.Notice (Title, Notice)  VALUES (%s, %s)"

        val = (Title, Notice)

        cur.execute(sql, val)
        DB.commit()
        return json.dumps ("{'data' : '게시글이 올라갔습니다.'}")


@app.route("/Title_DB",methods=['POST']) # 제목 찾기
def Title_DB():
    if request.method == 'POST':
        i = request.get_json()
        sql_Title = i.get('Title')

        DB = pymysql.connect(host='192.168.0.28',user='root',password='1234',db='DW_test',charset='utf8')  
        sql = DB.cursor()
        sql.execute("select * from DW_test.Notice where Title='"+sql_Title+"'")
        sql.execute("SELECT * FROM Notice WHERE Title LIKE'%"+sql_Title+"%'") # 특정단어 검색용도이나 도저히 사용 못하겠음
        data = json.dumps(sql.fetchall(),default=str)
        return data
'''


@app.route("/Check_Login",methods=['POST']) # 로그인
def Check_Login():
    if request.method == 'POST': # POST방식으로 들어온 데이터가 있다면 다음과 같이 실행하라
        i = request.get_json()
        ID = i.get('ID')
        PW = i.get('PW')

        DB = pymysql.connect(host='192.168.0.28',user='root',password='1234',db='id_data',charset='utf8')  

        cur = DB.cursor()
        query ="SELECT * FROM data"
        cur.execute(query)

        data_ID = 0
        data_PW = 0
        datas = cur.fetchall()
        for data in datas:
            if ID == (data[0]) and PW == (data[1]):
                data_ID = data[0]
                data_PW = data[1]
                data_Name = data[3]

        if not ID:
            return json.dumps("아이디를 입력해 주세요")
        elif not PW:
            return json.dumps("비밀번호를 입력해주세요")
        elif PW != data_PW:
            return json.dumps("비밀번호가 일치하지 않습니다.")
        else:
            session['login_ss'] = 1
            session['User_ID'] = data_ID
            session['User_PW'] = data_PW
            session['User_Name'] = data_Name
            # print('----------session------------')
            # print(session.get('User_ID'))

            sql = DB.cursor()
            sql.execute("select * from id_data.data where ID='"+ID+"' and PW='"+PW+"'")
            data = json.dumps(sql.fetchall(),default=str) # js로 데이터 반환할시 return data 사용
            # return json.dumps("로그인되었습니다.")
            # return render_template(Test_Page())
            # return redirect(url_for('Test_Page'))
            return data
        


@app.route("/Information",methods=['POST']) # 회원가입시 ID중복방지
def Information():
    if request.method == 'POST': # POST방식으로 요구
        i = request.get_json() # json타입으로 정보가져와 i에 대입
        ID = i.get('ID')
        PW = i.get('PW')
        Re_PW = i.get('Re_PW')
        Name = i.get('Name')

        DB = pymysql.connect(host='192.168.0.28',user='root',password='1234',db='id_data',charset='utf8')  
        
        cur = DB.cursor()
        query ="SELECT * FROM data"
        cur.execute(query)

        data_ID = 0
        datas = cur.fetchall()
        for data in datas:
            if ID == (data[0]):
                data_ID = ID

        if not(ID and PW and Re_PW and Name):
            return json.dumps("입력되지 않은 정보가 있습니다.")
        elif PW != Re_PW:
            return json.dumps("비밀번호가 일치하지 않습니다.")
        elif ID == data_ID:
            return json.dumps("중복되는 아이디입니다.")
        else:
            sql = "INSERT IGNORE INTO id_data.data (ID,PW,Re_PW,Name)  VALUES (%s, %s, %s, %s)"

            val = (ID,PW,Re_PW,Name)

            cur.execute(sql, val)
            DB.commit()
            return json.dumps("{'회원가입이 되었습니다.'}")


@app.route("/Ch_information",methods=['POST']) # 유저 정보 변경
def Ch_information():
    if request.method == 'POST': # POST방식으로 요구
        i = request.get_json() # json타입으로 정보가져와 i에 대입
        Ch_PW = i.get('Ch_PW')
        Ch_RePW = i.get('Ch_RePW')

        DB = pymysql.connect(host='192.168.0.28',user='root',password='1234',db='id_data',charset='utf8')  
      
        cur = DB.cursor()
        if not(Ch_PW and Ch_RePW):
            return json.dumps("입력되지 않은 정보가 있습니다.")
        elif Ch_PW != Ch_RePW:
            return json.dumps("비밀번호가 일치하지 않습니다.")
        else:
            cur.execute("update id_data.data set PW = '"+Ch_PW+"' where ID = '"+session['User_ID']+"'")
            # cur.excute update id_data.data set PW = '1234' where ID = '1234'
            DB.commit()
            return json.dumps("{'개인정보가 수정되었습니다.'}")



@app.route("/Upload_Notice",methods=['POST']) # 게시글 업로드
def Upload_Notice():
    if request.method == 'POST': # POST방식으로 요구
        i = request.get_json() # json타입으로 정보가져와 i에 대입
        Notice_Title = i.get('Notice_Title')
        Notice = i.get('Notice')
        Today = i.get('today')

        DB = pymysql.connect(host='192.168.0.28',user='root',password='1234',db='id_data',charset='utf8')  
        
        cur = DB.cursor()

        if not(Notice_Title):
            return json.dumps("제목을 입력해주세요.")
        elif not(Notice):
            return json.dumps("내용을 입력해주세요.")
        else:
            sql = "INSERT IGNORE INTO id_data.notice (ID,Name,Title,Notice,today)  VALUES (%s, %s, %s, %s, %s)"
            
            # cur.execute("update notice set Views= 0")

            val = (session['User_ID'], session['User_Name'], Notice_Title, Notice, Today)

            cur.execute(sql, val)
            DB.commit()

            return json.dumps("{'게시글올라감'}")
    
@app.route("/Return_Session",methods=['POST']) # 파이썬 session값 js로 보내기
def Return_Session():
    if request.method == 'POST': # POST방식으로 요청이 오면
        i = request.get_json()
        view = i.get('view')
        id = session.get('User_ID') 

        session['view'] = view
        DB = pymysql.connect(host='192.168.0.28',user='root',password='1234',db='id_data',charset='utf8')  
      
        # sql = "SELECT * FROM id_data.Notice where ID = %s"
        
        sql = DB.cursor()
        sql.execute('select * from id_data.notice')
        data = json.dumps(sql.fetchall(),default=str)

        sql.execute("select * from id_data.notice where ID='"+id+"'")
        # data = json.dumps(sql.fetchall(),default=str)

        DB.commit()
        # with DB: # seeeion사용시 이용
        #     with DB.cursor() as cur:
        #         cur.execute(sql,(id))
        #         result = cur.fetchall()

        #         for data in result:
        #             session['Title'] = data
        
        return  json.dumps(data)

        # return json.dumps({'ID' : id},{'Title' : title})


@app.route("/Read_Text",methods=['POST']) # 게시글 본내용 보기
def Read_Text():
    if request.method == 'POST':
        i = request.get_json()
        Title = i.get('Title')

        DB = pymysql.connect(host='192.168.0.28',user='root',password='1234',db='id_data',charset='utf8')  
        sql = DB.cursor()

        # sql.execute("select * from id_data.notice where Title='"+Title+"'")
        sql.execute('update notice set Views= Views + 1 where Title= "%s"' %Title)
        sql.execute('select * from id_data.notice where Title= "%s"' %Title)
        
        # sql.execute("update notice set View= ? where Title= ?", (View, Title))
        DB.commit()
        data = json.dumps(sql.fetchall(),default=str)
        return data


@app.route("/InitInfo_View",methods=['POST']) # View 정보 0변환
def InitInfo_View():
    if request.method == 'POST': # POST방식으로 요구
        i = request.get_json() # json타입으로 정보가져와 i에 대입
        View = i.get('data')

        DB = pymysql.connect(host='192.168.0.28',user='root',password='1234',db='id_data',charset='utf8')  
        
        cur = DB.cursor()

        # cur.execute("update notice set Views= 0") # 게시글 업로드시 (NULL)정보 0변환시키는것이나 
                                                    # 웹페이지 새로고침시 DB정보 초기화됨
        
        DB.commit()

        return json.dumps("{'DB정보 View 등록'}")

if __name__ == '__main__':

    app.run(host='0.0.0.0',port=5000, threaded=True)
    
    #os.execl(sys.executable, sys.executable, *sys.argv)
