from multiprocessing import Process
import random
import time
onegin=open('Онегин.txt','r')
onegin=onegin.readlines()
def create_file(n):
    kol=random.randrange(100,10000)
    file=open(('file'+str(n)+'.txt'),'a+')
    for i in range(kol):
        line=random.randrange(1,111)
        file.write(onegin[(line)])
    file.close()
start=time.time()
for i in range(100):
    create_file(12345678+i)
end=time.time()
print(end-start)
print('введите кол-во процессов: ')
kol_p=int(input())
a=[]
for i in range(5):
    p = Process(target=create_file, args=(i+1,))
    a.append(p)
    p.start()
start=time.time()
[multiprocessing.join() for multiprocessing in a]
end=time.time()
print(end-start)
 