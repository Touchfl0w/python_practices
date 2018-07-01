import schedule
import time

def job():
	print("*****")

schedule.every(6).seconds.do(job)

while True:
	#起始时刻开始标0，此时没有即将发生的job
	#run_pending方法意为：运行此时此刻日程上的job，显然当前无job
	schedule.run_pending()
	#对于已经错过的时刻，run_pending方法默认补救一次
	#例如，下例中sleep六秒，已经错过了第五秒，但要执行一次job;循环一圈第十二秒时，错过了第十秒，但可以补救一次job
	#但假若sleep函数的参数为12，则在第十二秒，错过了两次job,近补救一次
	time.sleep(6)
