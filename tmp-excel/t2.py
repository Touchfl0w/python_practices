import xlwt

#构造book
wbook = xlwt.Workbook()
sheet1 = wbook.add_sheet('sheet1')
#write(行，列，值)
sheet1.write(0,0,'kesjsjjs')
#保存
wbook.save('/home/openlab/Desktop/111.xls')