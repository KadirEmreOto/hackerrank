
n, k = map(int, raw_input().split())
a, b = map(int, raw_input().split()), int(raw_input())
answ = b - (sum(a) - a[k]) / 2 

print answ if answ else 'Bon Appetit'

