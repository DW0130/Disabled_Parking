

# 1. 인식된 번호를 좌측에서부터 7자리,8자리를 찾기
# 2. 번호의 기준이 되는 글자 찾기
# 3. 인식된 번호에서 기준이된 글자를 제외한 글자가 나오는지 확인후 기준이된 번호만 있다면 다음진행 아니면 다시 찾기
# 4. 기준이된 글자가 7자리번호의 글자위치인지, 8자리번호의 글자위치인지 확인
# 5. 결과값 출력



######## 함수사용

from itertools import count
from multiprocessing.sharedctypes import Value
from pydoc import text
import re
from tracemalloc import start

#num = "45가7715" #45가7715
#num = "385호6523" #385호6523
#num = "1이305다9437나1" #305다9437
#num = "1니85저4128" # 85저4128 오류
num = "경기45바4456" #경기45바4456

# 오류발생
#num = "1경기75사090111" #경기75사0901
#num = "1145가7715"
print("===========입력 정보============")
print(num) # 입력된 번호판 값

string = num
C_Num = re.findall('\w', string) # 문자열 -> 문자만 # re.findall('\w', string)  = 1개씩 분리



def AddSearch(data):

    if(data.isdigit()):
        if(data == 1):
            k = 0
        else: 
            k = 1
        return k
    elif(data.isalpha()):
        k = 0
        return k

    
def Old_Num():

    for n in range(10):
        
        start = 0 + n
        end = 7 + n
        exit = 0
        
        for data1 in num:

            Check_data = 0
            if(data1.isalpha()):
                Check_data = data1
                main_data = num[start:end]
                Num_check = num[start -1]
                
                i = 0
                for data2 in main_data:
                    if(data2.isalpha()):
                        if(data2 != Check_data): i = 1

                if(Num_check <= '4'):i = AddSearch(Num_check)

                Text_Val = start + 2
                if Text_Val == num.index(Check_data):
                    if (i == 0):
                        
                        print("===========최종결과============") 
                        print("구형")  
                        print("결과", main_data) 

                        exit = 1
                    
                    if(exit == 1): 
                        Plan = 1
                        return Plan
                    else:
                        Plan = 0
                        return Plan
            if(exit == 1): break
                
        if(exit == 1): break


def New_Num():

    for n in range(10):
        
        start = 0 + n
        end = 8 + n
        exit = 0
        # print("신형")
        # print(n,"번실행")
        # print("------------------")
        
        for data1 in num:

            Check_data = 0
            if(data1.isalpha()):
                Check_data = data1
                main_data = num[start:end]
                
                i = 0
                for data2 in main_data:
                    if(data2.isalpha()):
                        if(data2 != Check_data): i = 1
                if(i == 0):
                    Text_Val = start + 3
                    if Text_Val == num.index(Check_data):
                        
                        print("===========최종결과============") 
                        print("신형")  
                        print("결과", main_data) 
                        
                        exit = 1

            if(exit == 1): break
        if(exit == 1): break


def Business_Num():
    
    for data in num:
        
        Check = 0
        if(data.isalpha()):
            # Check_data = data1
            location_data = num.find(data)
            Check = 1

            if(Check == 1): break

    text1 = num[location_data]
    text2 = num[location_data +1]
    
    if(text1.isalpha() and text2.isalpha()):
        for n in range(10):
            
            start = 0 + n
            end = 7 + n
            exit = 0
            
            for data1 in num:

                Check_data = 0
                if(data1.isalpha()):
                    Check_data = data1
                    main_data = num[start:end]
                    Num_check = num[start -1]
                    
                    i = 0
                    for data2 in main_data:
                        if(data2.isalpha()):
                            if(data2 != Check_data): i = 1

                    i = AddSearch(Num_check)

                    Text_Val = start + 2
                    if Text_Val == num.index(Check_data):
                        if (i == 0):
                            
                            print("===========최종결과============") 
                            print("사업용")  
                            print("결과", text1 + text2 + main_data) 

                            exit = 1
                        
                        if(exit == 1): 
                            Plan = 1
                            return Plan
                        else:
                            Plan = 0
                            return Plan
                if(exit == 1): break
                    
            if(exit == 1): break
    else:
        Plan = 0
        return Plan
        




Plan = Business_Num()
if(Plan == 0): Old_Num()
if(Plan == 0): New_Num()