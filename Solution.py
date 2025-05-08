# cook your dish here
cases = int(input())
for c in range(cases):
    n, x = map(int, input().split())
    cost = x
    while n > 6:
        cost = cost + x
        n = n - 6
    print(cost)
