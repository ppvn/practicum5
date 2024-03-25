b1, b2, b3 = map(int, input().split())

a = [b1, b2, b3]
mx = max(a)
a.remove(max(a))

print(mx, max(a), min(a))