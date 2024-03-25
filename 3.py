num = int(input())
dig1 = num // 1000
dig2 = (num // 100) % 10
dig3 = (num % 100) // 10
dig4 = num % 10
if dig1 == dig4 and dig2 == dig3:
    print('Настоящее')
else:
    print('Кривое')