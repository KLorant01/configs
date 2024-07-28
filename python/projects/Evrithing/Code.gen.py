import random

kys = '0123456789qwertzuiopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM?!,.:-_%/*+=()€[]$<>#&@{};?!,.:-_%/*+=()€[]$<>#&@{};'
#114 darab karakter.

psw_lenght, psw = int(input('Psw hossza:\n')), ''
print('\n')
for _ in range(psw_lenght):
    num = random.choice(kys)
    psw = psw + num
print(psw)