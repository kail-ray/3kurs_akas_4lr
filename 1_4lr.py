import random
import time
import threading
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
create_file(123456789)
create_file(123456788)
create_file(123456786)
create_file(123456785)
end=time.time()
print(end-start)
print('введите кол-во пoтоков: ')
kol_p=int(input())
threads = []
for i in range(kol_p):
    t = threading.Thread(target=create_file, args=(i+1,))
    threads.append(t)
    t.start()
start=time.time()
[thread.join() for thread in threads]
end=time.time()
print(end-start)