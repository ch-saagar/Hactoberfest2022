import bisect
m = [1, 3, 7, 5, 6, 4, 9, 8, 2]

result = []
for i in m:
    bisect.insort(result, i)

print(result)
