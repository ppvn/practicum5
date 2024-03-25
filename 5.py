weight = int(input('Введите вес, кг: '))
height = int(input('Введите рост, см: ')) / 100
bmi = (weight/(height**2))

if bmi < 16:
    print('Выраженный дефицит массы тела')
elif 16 <= bmi <= 18.49:
    print('Недостаточная масса тела')
elif 18.50 <= bmi <= 24.99:
    print('Норма')
elif 25 <= bmi <= 29.99:
    print('Избыточная масса тела')
elif 30 <= bmi <= 34.99:
    print('Ожирение первой степени')
elif 35 <= bmi <= 39.99:
    print('Ожирение второй степени')
else:
    print('Ожирение третьей степени')