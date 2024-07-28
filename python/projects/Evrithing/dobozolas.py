from typing import List, Any

targyak = [16, 8, 9, 4, 3, 2, 4, 7, 7, 12, 3, 5, 4, 3, 2]
dobozok = [0]
db = 0

for i in targyak:
    if dobozok[db] + i > 20:
        db += 1
        dobozok.append(0)

    dobozok[db] = dobozok[db] + i

print("dobozok szama: ", len(dobozok))
print("dobozok tartalma: ")
print(dobozok)
