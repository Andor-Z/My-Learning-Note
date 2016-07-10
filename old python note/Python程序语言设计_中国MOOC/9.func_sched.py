#9.func_sched.py

import sched, time
def print_time(msg = 'default'):
	print('当前时间  ', time.time(), msg)

s = sched.scheduler(time.time, time.sleep)
print(time.time())
s.enter(5, 1, print_time, argument=('延迟5秒，优先级1',))
s.enter(3, 2, print_time, argument=('延迟3秒，优先级2',))
s.enter(3, 1, print_time, argument=('延迟3秒，优先级1',))
s.run()
print(time.time())