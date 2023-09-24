import xlsxwriter

workbook = xlsxwriter.Workbook("Allablotpython.xlsx")
worksheet = workbook.add_worksheet("firstsheet")

worksheet.write(0,0,"#")
workbook.close()