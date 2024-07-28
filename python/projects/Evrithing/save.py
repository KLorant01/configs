with open('data.txt','w') as F: pass

#ideiglenes cuccok
with open('data.txt','w') as F:
    F.write('''numerouno€1$
duo€12$
trio€123$
lol€fasz$
imi€dazol$''')

# namme€adat1$adat2$adat3... stb

def READ(need):
    with open('data.txt', 'r') as Fuck:
        for line in Fuck:
            if line.count(need) == 1:
                return line[line.find('€')+1:line.find('$')]
        return False

def Find(change):
    with open('data.txt', 'r') as Fuck:
        num = 0
        for line in Fuck:
            num += 1
            if line.count(change) == 1:
                return line, num

def Write(change, new_val):
    line, num = Find(change)[0], Find(change)[1]
    with open('data.txt', 'w') as Fuck:
        for i in range(num):
            Fuck.readline()
        print(Fuck.readline())

def WriteNew(new_thing):
    with open('data.txt', 'a') as Fuck:
        Fuck.write('\n' + new_thing)

#print(READ('alakoskodas'))