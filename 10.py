pin = int(input())

dig1 = pin // 1000
dig2 = (pin // 100) % 10
dig3 = (pin % 100) // 10
dig4 = pin % 10

pin1 = set([dig1, dig2, dig3, dig4])
if len(pin1) == 4 and not (1900 <= pin <= 2050):
    print('OK')
else:
    print('ERROR')
    