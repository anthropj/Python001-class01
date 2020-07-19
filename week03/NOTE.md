学习笔记



进程的创建

```python
# 进程的创建，函数创建的方式
from multiprocessing import Process

def func(*args, **kwargs):
    pass

if __name__ == "__main__":
    # Process(group, target, name, args, kwargs)
    # 常用参数: target为函数对象，args存放元组值，kwargs存放字典值
    p = Process(target=func, args=(args1,))
    p.start()			# 启动进程
    p.join([timeout])			# 使父进程等待子进程进行结束 
    
# 一些关于multiprocessing调试相关的函数
# multiprocessing.active_children()返回的是活动进程的迭代器
# 每个活动对象都有name以及pid属性
# multiprocessing.cpu_count()返回的本机cpu的核心数，更好地设置进程并发的数量
# 关于os模块的一些函数 os.getppid(), os.getpid()分别取得父进程以及当前进程的id

# 进程的创建， 类继承的方式
class NewClassName(Process):
    def __init__(self, args1):
        self.args1 = args1
        super().__init__()
      
    # 当实例化进程新类的时候会自动调用run方法，所以要重写该方法
    def run(self):
        pass
    
p = NewClassName(args)
p.start()
```



进程间的通信

```python
# 队列方式 (queue)
# queue method: put, get
from multiprocessing import Process, Queue

# 目标对象对queue进行操作
def f(q):
    q.put(Iterable)

if __name__ == '__main__'：
	q = Queue()
    # 子进程传入queue
    p = Process(target = f, args = (q,))
    p.start()
    # 父进程调用queue
    print(q.get())
    p.join()
```



进程的锁机制

```python
# 将锁作为一种共享变量在各个进程间传递
import multiprocessing as mp

def job(v,num,l):
    l.acquire()		# 上锁
    for _ in range(5):
        v.value += num
    l.release()		# 解锁
    
def multicore():
    l = mp.Lock()	# 进程锁
    v = mp.Value('i', 0)	# 共享内存机制, Value(type, num)
    
    p1 = mp.Process(target=job, args=(v,1,l))	# 将进程锁作为参数传递
    p2 = mp.Process(target=job, args=(v,3,l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
```



进程池

```python
# 不带with标识符
from multiprocessing.pool import Pool

def fun1():
    pass

if __name__ == '__main__':
    p = Pool(processes = 4)
    for _ in range(10):
        p.apply_async(fun1)		# apply_async(func_object, args)
    p.close()
    p.join()
    
# 带with标识符的
with Pool(processes = num) as pool:
    result = pool.apply_async(fun_obj, args)
    print(result.get(timeout = num))
    
with Pool(processes = num) as pool:
    print(pool.map(fun_obj, Iterable))
```



线程的创建

```python
# 函数的方式
import threading

def fun1(args):
    pass

if __name__ == '__main__':
    t1 = threading.Thread(target = fun1, args)
    t1.start()
    
# 面向对象的方式
class MyThread(threading.Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n
       
    # need to overwrite
    def run(self):
        pass
    
if __name__ == '__main__':
    t1 = MyThread(args)
    t1.start()
    t1.join()
    
# 线程自带的方法
# thread.is_alive()/getName()
```



线程锁机制

```python
import threading

lock = threading.Lock()			# 需要嵌套锁的话就是RLock

class MyThread(threading.Thread):
    def run(self):
        if lock.acquire(1):
            pass
        lock.release()

# 条件锁
lock = threading.Condition()
lock.wait()			# 等待
lock.wait_for(fun_object)		# fun_object need return bool
lock.notify()		# 通知其他线程
```



