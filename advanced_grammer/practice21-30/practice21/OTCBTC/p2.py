from threading import Thread

class DownloadThread(Thread):
	'''下载当前某种货币的卖单与买单'''
	def __init__(self,coin_id):
		Thread().__init__(self)
		self.coin_id = coin_id

	def run(self):
		self.download(url)

