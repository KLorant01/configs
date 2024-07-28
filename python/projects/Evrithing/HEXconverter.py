caracters = []

for i in '0123456789abcdef':
    caracters.append(i)

operation = str(input("Convert to: "))
operation.lower()
if operation.startswith("h"):
    num = int(input("DEC: "))
    num2 = ""
    for i in range(20, 0):
        if (num//16**i) > 0:
            num2+=caracters[(num//16**i)]
            num -= 16**i
    print(f"HEX: {num2}")
else:
    num = str("HEX: ")