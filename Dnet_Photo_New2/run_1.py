#This is a python
from flask import Flask,render_template,request,send_file,redirect,session,flash

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

@app.route("/") # 프로그램 시작시 먼저 실행
def main():
    return render_template('test_excel.html')



@app.route("/Registration",methods=['POST']) # 정보등록
def Registration():

    if request.method == 'POST': # POST방식으로 요구
        i = request.get_json() # json타입으로 정보가져와 i에 대입
        Name = i.get('Name')
        ID = i.get('ID')
        Birth_Year = i.get('Birth_Year')
        Phone = i.get('Phone')
        DB = pymysql.connect(host='192.168.0.28',user='root',password='1234',db='DW_test',charset='utf8')  
        cur = DB.cursor()
        sql = "INSERT IGNORE INTO id_data.data (Name, ID, Birth_Year, Phone)  VALUES (%s, %s, %s, %s)"

        val = (Name, ID, Birth_Year, Phone)

        cur.execute(sql, val)
        DB.commit()
        return json.dumps ("{'data' : '게시글이 올라갔습니다.'}")

        
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

