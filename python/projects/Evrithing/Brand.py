import random

kys = 'QWERTZUIOPASDFGHJKLYXCVBNM'
#114 darab karakter.

psw_lenght, psw = int(input('Brand hossza:\n')), ''
print('\n')
for _ in range(psw_lenght):
    num = random.choice(kys)
    psw = psw + num
print(psw)