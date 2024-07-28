Valtozok = ["Rash", "Kil", "Varsha"]
kulcsok = [1, 4, 5]

res = {}
for key in Valtozok:
    for value in kulcsok:
        res[key] = value
        kulcsok.remove(value)
        break

print(res)