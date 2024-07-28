num = int(input(":\n"))
hatvany, value = 1, ''

while 2**hatvany <= num:
    a = 0
    value = str(num/(2**hatvany))
    for i in value:
        if not i == '.':
            a += int(i)
    if a % 9 == 0:
        print(F"{2**hatvany} | oszthato")
    else:
        print(F"{2**hatvany} | nem oszthato")
    hatvany += 1
