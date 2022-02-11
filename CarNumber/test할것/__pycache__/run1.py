
from cgitb import text
from doctest import testfile
from itertools import count
from multiprocessing.sharedctypes import Value
import re
from tabnanny import check
from this import d
from tracemalloc import stop

num = "145가77115" #45가7711
#num = "1이305다9437나1" #305다9437
#num = "경기45바4456" #경기45바4456
#num = "11경기75사090111" #경기75사0901
print("==========================")
print("입력된 정보: ", num) # 입력된 번호판 값
print("==========================")

j = 0

#7자리의 좌측 끝 -1부분의 정보확인
def AddSearch(data):
    
    if (data.isalpha() == False):

        val = re.findall(r'\d',data)
        print(val)
        if(val[0] == '1'):
            i = 0
            return i
        elif(val[0] != '1'):
            i = 1
            return i
    else:
        i = 1
        return i


#7자리일경우
def NumList7():

    for n in range(10):
    
        exit = 0  
    
        start_1 = 0 + n
        end_1 = 7 + n
        
        for data in num: 
    
            i = 0 
            Check_data = 0 
            if(data.isalpha()): # 기준이 되는 글자 검색 
    
                Check_data = data 
                data1 = num[start_1:end_1] 
                numcheck = num[start_1 -1]

            if(Check_data != 0): 
                for data in data1: 
                    if(data.isalpha() != Check_data): i = 1 # 7자리 번호, 기준글자와 중복방지 
    
                i = AddSearch(numcheck)

                if(i == 0): # 번호리스트에서 기준글자만 있는경우, 현 리스트에서 좌측 3번째 위치에 글자가 오도록 유도할것 
                    
                    Value = start_1 + 2 
                    if Value == num.index(Check_data): 

                        
                        print("==========================") 
                        print("기준 글자 : ", Check_data) 
                        print("7자리") 
                        Result = ''.join(data1) 
                        print(Result) 
                        print("==========================") 
                        exit = 1 
                        test_i = 1
                        return test_i
                    else:
                        test_i = 0
                        return test_i
                
            if(exit == 1): return test_i
        if(exit == 1): return test_i
    if(exit == 1): return test_i

#8자리일경우
def NumList8():
    for n in range(10):  

        exit = 0  

        start_2 = 0 + n 
        end_2 = 8 + n 
        
        for data in num: 
    
            Check_data = 0 
            if(data.isalpha()): # 기준이 되는 글자 검색 
    
                Check_data = data 
                data2 = num[start_2:end_2] 
    
            if(Check_data != 0):                    
    
                i = 0 
                for data in data2: 
                    if(data.isalpha()): # 8자리 번호, 기준글자와 중복방지 
                        if (data != Check_data): i = 1 
    
                if(i == 0): # 번호리스트에서 기준글자만 있는경우, 현 리스트에서 좌측 3번째 위치에 글자가 오도록 유도할것 
                    
                    Value = start_2 + 3 
                    if Value == num.index(Check_data): 
                        
                        print("==========================") 
                        print("기준 글자 : ", Check_data) 
                        print("8자리") 
                        Result = ''.join(data2) 
                        print(Result) 
                        print("==========================") 
                        exit = 1 
            if(exit == 1): break  #if(C_data == 1): 
        if(exit == 1): break 


j = NumList7()

if(j == 0) :NumList8()