import time

def fibonachi(n: int) -> int:
    num1: int = 1
    num2: int = 1
    buffer: int
    for _ in range(n - 1):
        buffer = num2
        num2 = buffer + num1
        num1 = buffer

    return num2


act_time = time.time()

for i in range(5000):
    print(fibonachi(i))

dif_time = time.time() - act_time
print(dif_time)
