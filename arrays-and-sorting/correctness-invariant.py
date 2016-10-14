n = raw_input()
ar = [int(i) for i in raw_input().strip().split()]
ar.sort()
print " ".join(map(str,ar))

