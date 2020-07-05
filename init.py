import kaktovik
import time

start = time.time()

while (True):
    now = time.time()
    delta_seconds = now - start
    print(u''+kaktovik.convertDec(int(delta_seconds)))
    time.sleep(1)

    
