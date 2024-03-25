kn = int(input('Введите кнаты\n'))

gl = kn // (29 * 17)
kn_left = (kn - (gl * 17 * 29))
sikl = (kn - (gl * 17 * 29)) // 29

if gl != 0: print(gl, 'галлеонов')
if sikl != 0: print(sikl, 'скилев')
if kn_left != 0: print(kn_left, 'кнатов')