import time

pi = 0
num = 0

rec = time.time()

for _ in range(100000000):
    if num % 2 == 0:
        pi += (4/(2*num+1))
    else:
        pi -= (4 / (2 * num + 1))
    num += 1
print(pi)
