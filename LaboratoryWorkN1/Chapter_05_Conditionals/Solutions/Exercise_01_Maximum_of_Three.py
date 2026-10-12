a, b, c = map(int, input().split())
if a >= b and a >= c:
    result = a
elif b >= a and b >= c:
    result = b
else:
    result = c
print(result)
