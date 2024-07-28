import random
Anna_win, Panna_win, N, sum = 0, 0, int(input("Hanyszor dobjanak")), 0
for f in range(N):
    for _ in 'abc': sum += random.randint(1,6);
    print(f"A dobás eredménye: {sum}")
    if sum < 10: Anna_win += 1; sum = 0
    else: Panna_win += 1; sum = 0
print(f"Anna nyert: {Anna_win}\nPanna nyert: {Panna_win}")