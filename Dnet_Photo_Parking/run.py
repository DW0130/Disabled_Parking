from unittest import result
from flask import Flask,render_template,request,send_file,redirect,session,flash

from werkzeug.utils import secure_filename
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


@app.route("/")
def main():
    return render_template('login.html')
    
@app.route("/login",methods=['POST'])
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

@app.route("/list")
def listmain():
    if (session.get('login')) :
        return render_template('main.html')
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
        
@app.route("/searchDB",methods=['POST'])
def searchDB():
    if request.method == 'POST':
        i = request.get_json()
        
        print("====================================")
        print(i.get('startdate'))
        print(i.get('enddate'))
        print(i.get('cnum'))
        print(i.get('location'))
        print("====================================")

        DB = pymysql.connect(host='127.0.0.1',user='root',password='1234',db='parking',charset='utf8')  
        sql = DB.cursor()
        # AND Number ="+i.get('cnum')+" 차량번호쪽 오류(추후 추가할 예정)
        sql.execute("select * from photo")

        with DB:
            with 
        
        sql.execute("select LCT,SPD,TME,PHT from speeddb.CarDB where TME between '"+i.get('startdate')+"' and '"+i.get('enddate')+"' AND SPD >"+i.get('lim')+" AND LCT ='"+i.get('location')+"' ORDER BY TME DESC")
        data = json.dumps(sql.fetchall(),default=str)
        
        print("====================================")
        print(data)
        print("====================================")


        return data






if __name__ == '__main__':

    app.run(host='0.0.0.0',port=5000, threaded=True)
    
    #os.execl(sys.executable, sys.executable, *sys.argv)