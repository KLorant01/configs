import math

ALL_OP = '+-*/er'
form = []
NUMS = '0123456789'

def osszeadas(X, Y):
    return X + Y

def kivonas(X, Y):
    return X - Y

def szorzas(X, Y):
    return X * Y

def osztas(X, Y):
    return X / Y

def hatvany(X, Y):
    return X ** Y

def sqr(X, Y):
    if Y == 2:
        return math.sqrt(X)
    return math.sqrt(Y)

def gyok(X, Y):
    return X ** (1 / Y)

def popp(dat, k):
    for times in '123':
        dat.pop(k)
    return dat

def check(raw_form):  # ellenőrzés    ez még nem tőkéletes!!!!
    zjk = zjv = not_number = 0

    if ALL_OP.count(raw_form[-1]) == 1 or ALL_OP.count(raw_form[0]) == 1: return True  # Operátorral kezdődik

    if raw_form.count('(') != raw_form.count(')'): return True # Nem megfelelő zárójelezés

    for i in raw_form:
        if ALL_OP.count(i) == 0 and i not in NUMS and i != '(' and i != ')': return True  # Nemismert karakter

        if ALL_OP.count(i) == 1: not_number += 1
        else: not_number = 0

        if not_number == 2: return True  # Operátorok egymás mellett
    return False

def cut(raw_form):  # A képlet elemzése:  Pipa
    ertek, form = '', []
    for i in raw_form:
        if i not in NUMS:
            if ertek != '':
                form.append(int(ertek))
            ertek = ''
            form.append(i)
        else:  ertek = ertek + i
    if ertek != '':
        form.append(int(ertek))
    return form

def zf(form):
    inside = []
    for g in form:
        if g == ')':
            elem = form.index(')')
            for i in form[form.index(')')::-1]:
                inside.insert(0, i)
                form.pop(elem)
                elem -= 1
                if i == '(':
                    form.insert(elem + 1, calculate(inside[1:-1])[0])
                    return form

def calculate(el):
    while el.count('e') == 1 or el.count('r') == 1:
        f = -2

        for i in el:
            f += 1
            if i == 'e':
                el.insert(f + 3, hatvany(el[f], el[f + 2]))
                el = popp(el, f)

            if i == 'r' and (el[f] == 2 or el[f + 2] == 2):
                el.insert(f + 3, sqr(el[f], el[f + 2]))
                el = popp(el, f)

            elif i == 'r':
                el.insert(f + 3, gyok(el[f], el[f + 2]))
                el = popp(el, f)

    while el.count('*') == 1 or el.count('/') == 1:
        f = -2

        for i in el:
            f += 1

            if i == '*':
                el.insert(f + 3, szorzas(el[f], el[f + 2]))
                el = popp(el, f)

            if i == '/':
                el.insert(f + 3, osztas(el[f], el[f + 2]))
                el = popp(el, f)

    while el.count('+') == 1 or el.count('-') == 1:
        f = -2

        for i in el:
            f += 1

            if i == '+':
                el.insert(f + 3, osszeadas(el[f], el[f + 2]))
                el = popp(el, f)

            if i == '-':
                el.insert(f + 3, kivonas(el[f], el[f + 2]))
                el = popp(el, f)
    return el

raw_form = str(input('Adjon meg egy kifejezést!:\n'))  # A folyamatok elvégzése

if check(raw_form): print('nem jó')

else:
    form = cut(raw_form)
    for i in form:
        if i == ')': form = zf(form)
    form = calculate(form)

print(form[0])

