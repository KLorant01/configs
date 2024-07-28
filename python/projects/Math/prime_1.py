import time

prime_Table: list = []
ctr_Table: list = []
place: int = 0
prime: bool = True
num: int = 2
end: int = int(input(": "))

act_time = time.time()

while num < end+1:
    prime = True

    for i in ctr_Table:
        if i == num:
            place = ctr_Table.index(i)
            ctr_Table[place] += prime_Table[place]
            prime = False
        elif not prime:
            break

    if prime:
        prime_Table.append(num)
        ctr_Table.append(num**2)

    num += 1
d_time = time.time() - act_time

print(prime_Table)
print("")
print(d_time)
