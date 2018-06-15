import struct 
from collections import namedtuple
import array

class Wav():
	def __init__(self,filename,filename_tosave):
		#虽然在类的其他方法里创建self.avariable也会生成实例属性，但最好把多个方法公用的实例属性放在__init__里定义
		self.filename = filename
		self.filename_tosave = filename_tosave
		#由于python弱类型，这里用数字0初始化也没问题，但最好还是用空bytes比较规整
		self.head_bytes = b''
		self.myarray = array.array('h')
		self.myarray_length = 0

	def __parse(self):
		'''二进制数据读取为结构化bytes'''
		with open(self.filename,'rb') as rf:
			self.head_bytes = rf.read(44)
			rf.seek(0,2)
			self.myarray_length = int((rf.tell()-44)/2)
			self.myarray = array.array('h',(0 for _ in range(self.myarray_length)))
			rf.seek(44,0)
			rf.readinto(self.myarray)

	def __print_header(self):
		'''把header由bytes转化为Python数据类型并输出'''
		Header = namedtuple('Header','NumChanels SampleRate BitsPerSample')
		numchanels = struct.unpack('<h',self.head_bytes[22:24])
		samplerate = struct.unpack('<i',self.head_bytes[24:28])
		bitespersample = struct.unpack('<h',self.head_bytes[34:36])
		header = Header(numchanels,samplerate,bitespersample)
		#打印具名元组
		print(header)

	def __modify_wav(self):
		'''将wav文件音量调低'''
		for i in range(self.myarray_length):
			self.myarray[i] = int(self.myarray[i]/10)

	def __save(self):
		'''将修改的文件保存'''
		with open(self.filename_tosave,'wb') as wf:
			wf.write(self.head_bytes)
			self.myarray.tofile(wf)

	def go(self):
		#启动程序
		self.__parse()
		self.__print_header()
		self.__modify_wav()
		self.__save()

wav = Wav('1969.wav','demo1.wav')
wav.go()



