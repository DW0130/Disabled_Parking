
import re

num = "149우9815호1나"

print(num) # 입력된 번호판 값

string = num
#numbers = re.findall('\d+', string) # 문자열 -> 숫자만 
C_Num = re.findall('\w', string) # 문자열 -> 문자만 # re.findall('\w', string)  = 1개씩 분리

# print(numbers)
# print(C_Num) # 번호판 쪼개기

for data in C_Num:
    if(data.isalpha()): # 문자가 있는지 판별
        Check_Data = C_Num.index(data)
        if(C_Num[Check_Data -1]):
            
        
        # data1 = data
        
        break
print(Check_Data)
# in_data = C_Num.index(data1) # 좌측에서 첫번째 글자 위치

n = -1
while True:
    if C_Num[n+1:].count(0) == 0:
        break







list_a = [1, 1, 1, 2, 3, 4, 1, 5, 6, 1, 1]

n = -1
while True:
    if list_a[n+1:].count(1) == 0:
        break
    n += list_a[n+1:].index(1) + 1
    print(n, end=' ')
[출처] [python] list에서 특정값의 인덱스 찾기|작성자 피티아



# data2 = C_Num[in_data -1]
# data3 = C_Num[in_data -2]
# data4 = C_Num[in_data +1]
# data5 = C_Num[in_data +2]
# data6 = C_Num[in_data +3]
# data7 = C_Num[in_data +4]

# Car_Number = data3 + data2 + data1 + data4 + data5 + data6 + data7

# print(Car_Number)