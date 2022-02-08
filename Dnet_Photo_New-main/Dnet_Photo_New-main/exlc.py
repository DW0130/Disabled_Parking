#This is a Python!!!
import openpyxl

wb = openpyxl.Workbook()

wb.active.title = "감지 목록"
file = '/home/pi/Desktop/exal/ex.xlsx'
locat = 'A1'
detal = 'asdf'

w1 = wb["감지 목록"]
w1[locat].value = detal

wb.save(file)