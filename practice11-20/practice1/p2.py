import xlrd

class Compare_sheets():
	def __init__(self,sheet1,sheet2):
		self.sheet1 = sheet1
		self.sheet2 = sheet2
		

	def __sheet_to_set(self,sheet):
		tmpset = set()
		for row in range(1,sheet.nrows):
			info_tuple = tuple(sheet.row_values(row))
			tmpset.add(info_tuple)
		return tmpset

	def __compare_sets(self,set1,set2):
		if not set1-set2:
			print("sheet1中不同于sheet2的元素有： 空")
		else:
			print("sheet1中不同于sheet2的元素有：",set1-set2)
		if not set2 - set1:
			print("sheet2中不同于sheet1的元素有： 空")
		else:
			print("sheet2中不同于sheet1的元素有：",set2-set1)

	def go(self):
		set1 = self.__sheet_to_set(self.sheet1)
		set2 = self.__sheet_to_set(self.sheet2)
		self.__compare_sets(set1,set2)

rbook = xlrd.open_workbook('test.xlsx')
sheet1 = rbook.sheet_by_index(0)
sheet2 = rbook.sheet_by_index(1)
compare = Compare_sheets(sheet1,sheet2)
compare.go()
