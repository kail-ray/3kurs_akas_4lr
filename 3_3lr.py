import urllib.request
import threading
import time
urls = [
 'https://www.pnzgu.ru/',
 'https://moodle.pnzgu.ru/my/',
 'https://lk.pnzgu.ru/portfolio/my',
 ]
def urlstatus(url):
    with urllib.request.urlopen(url) as u:
        return u.getcode()
threads = []
start = time.time()
for url in urls:
    t = threading.Thread(target=urlstatus, args=(url,))
    threads.append(t)
    t.start()
    print(url,urlstatus(url))
[thread.join() for thread in threads]
print(time.time() - start)