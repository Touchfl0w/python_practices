from concurrent.futures import ThreadPoolExecutor

def handle(a,b):
	print('hello world',str(a*b))
	return a*b
#构建多线程对象：executor
executor = ThreadPoolExecutor(max_workers=3)
#调用submit方法，提交任务给线程池，默认一次submit使用一个线程
#线程执行结果由Future对象保存
future = executor.submit(handle,3,4)
#调用result方法提取结果，如果线程未结束，则阻塞起来，直到有结果
result = future.result()
print(result)

#除了submit，还有更高效的提交任务方法map，返回迭代器，每次迭代返回函数的执行结果，不是future对象
#使用3个线程，依次执行handle(1,1) handle(2,2) handle(3,3)
for result in executor.map(handle,[1,2,3],[1,2,3]):
	print(result)

