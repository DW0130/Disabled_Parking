

# 1. 인식된 번호를 좌측에서부터 7자리,8자리를 찾기
# 2. 번호의 기준이 되는 글자 찾기
# 3. 인식된 번호에서 기준이된 글자를 제외한 글자가 나오는지 확인후 기준이된 번호만 있다면 다음진행 아니면 다시 찾기
# 4. 기준이된 글자가 7자리번호의 글자위치인지, 8자리번호의 글자위치인지 확인
# 5. 결과값 출력


import re

num = "45가7715" #45가7715
num = "385호6523" #385호6523
num = "1이305다9437나1" #305다9437
num = "1니85저4128" # 85저4128 오류
num = "경기45바4456" #경기45바4456
num = "12경기75사090111" #경기75사0901
num = "대구42고7284" #대구42고7284
#num = "11145가7715" #145가7715

num = "145니85저4128" # 85저4128 오류

print("===========입력정보===========")
print(num) # 입력된 번호판 값




    
def Old_Num():

    for n in range(10):
        
        start = 0 + n
        end = 7 + n

        exit = 0
        Result = ''
        for data1 in num:

            Check_data = 0
            if(data1.isalpha()):
                Check_data = data1
                main_data = num[start:end]
                
                i = 0
                for data2 in main_data:
                    if(data2.isalpha()):
                        if(data2 != Check_data): i = 1

                Text_Val = start + 2
                if Text_Val == num.index(Check_data):
                    if (i == 0):

                        Result = num, main_data
                        exit = 1
            if(exit == 1): break
                
        if(exit == 1): break
    return Result


def New_Num():

    for n in range(10):

        start = 0 + n
        end = 8 + n

        exit = 0
        Result = ''
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
                        
                        Result = num, main_data
                        exit = 1
            
            if(exit == 1): break
    
        if(exit == 1): break
    return Result


def Business_Num():

    for data3 in num:

        exit = 0
        Result = ''
        if(data3.isalpha()):
            location_data = num.find(data3)
            text1 = num[location_data]
            text2 = num[location_data +1]
            if(text1.isalpha() and text2.isalpha()):

                for n in range(10):
                    start = num.find(text1) + n      
                    end = start + 7
                    
                    for data1 in num:

                        Check_data = 0
                        if(data1.isalpha()):
                            Check_data = data1
                            main_data = num[start:end]
                            
                            i = 0
                            for data2 in main_data:
                                if(data2.isalpha()):
                                    if(data2 != Check_data): i = 1

                            Text_Val = start + 2
                            if Text_Val == num.index(Check_data):
                                if (i == 0):
                                    
                                    Result = num, text1 + text2 + main_data
                                    exit = 1
        
                        if(exit == 1): break
                
                    if(exit == 1): break
        if(exit == 1): break
    return Result


DEV_SHOW_LOG = ''
Result = ''
Result = Business_Num()
if(Result.isalpha() == False): Result = New_Num()
if(Result.isalpha() == False): Result = Old_Num()

print(Result)