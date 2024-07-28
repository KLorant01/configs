from random import randint
import time

# hatoldalu kocka
A = B = C = D = E = F = 0
nums = [A, B, C, D, E, F]

num, rec = int(input(": ")), time.time()

for _ in range(num):
    val = randint(0, 5)
    nums[val] += 1

print(f'\n time: {time.time() - rec} sec\n')
for i in range(6):
    print(f'{i + 1}| {nums[i]} ', end='')
    for f in range(nums[i]):
        print('#', end='')
    print('')
