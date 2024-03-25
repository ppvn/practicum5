n, k, m = map(int, input().split())
if m > k:
    print(m-k-1)
if m < k:
    print(n-k+m)