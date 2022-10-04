

import openpyxl
from openpyxl.drawing.image import Image


# inserting image in the excel sheet


file="D:\Demofiles\imagecopy.xlsx"

workbook=openpyxl.load_workbook(file)
sheet=workbook["Sheet1"]

logo=Image("D:\Demofiles\logo.png")

logo.height=150
logo.width=150

sheet.add_image(logo,"A3")
workbook.save(file)