"""
excel操作
"""
import xlrd,xlwt
#读取excel文件
rbook = xlrd.open_workbook('grades.xls')
#读取sheet表
rsheet = rbook.sheet_by_index(0)
cols = rsheet.ncols
#修改sheet表
rsheet.put_cell(0,cols,1,'总分',None)
for row in range(1,rsheet.nrows):
	grade = sum(rsheet.row_values(row,1))
	rsheet.put_cell(row,cols,2,grade,None)


wbook = xlwt.Workbook()
#创建一张临时表，暂时为空
wsheet = wbook.add_sheet('sheet1')
#将修改过得rsheet赋值给临时表
for r in range(rsheet.nrows):
	for c in range(rsheet.ncols):
		wsheet.write(r,c,rsheet.cell(r,c).value)

wbook.save('grades1.xls')


