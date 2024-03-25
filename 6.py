d1 = int(input())
d2 = int(input())
d3 = int(input())

num = len(set([d1, d2, d3]))
match num:
    case 1:
        print(3)
    case 2:
        print(2)
    case 3:
        print(1)