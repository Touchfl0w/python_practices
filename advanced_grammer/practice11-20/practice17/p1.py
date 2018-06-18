#设置全缓冲，缓冲区大小2048byte
wf = open('demo1.txt','w',buffering=2048)
wf.write('#')
wf.write('*')