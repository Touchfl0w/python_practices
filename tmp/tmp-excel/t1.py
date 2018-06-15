import xlrd

#不可以使用～来代替/home/openlab
book = xlrd.open_workbook('/home/openlab/Desktop/test.xls')
#一个book含有两张sheet,可以看到返回了两个sheet object
print(book.sheets())
#取到book里的第一张sheet
sheet0 = book.sheet_by_index(0)
#查看sheet的行
print(sheet0.nrows)
#查看sheet的列
print(sheet0.ncols)
#访问cell,即一个小格
#返回类型+value
print(sheet0.cell(0,0))
#返回类型 1代表文本 2代表数字
print(sheet0.cell(0,0).ctype)
print(sheet0.cell(1,1).ctype)
#返回value
print(sheet0.cell(0,0).value)
#访sheet的行,行号从0开始
print(sheet0.row(1))
#访sheet的行,并对选中的行按列切片 row_values(行号，起始列号，终止列号=None)  注意：左闭右开
print(sheet0.row_values(1,1,None))
print(sheet0.col(0))
print(sheet0.col_values(0,1,None))

print(sheet0.cell(1,1))
sheet0.put_cell(1,1,2,100,None)
print(sheet0.cell(1,1))