a, b, c = map(float, input().split())
if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("не трикутник")
elif a == b == c:
    print("рівносторонній")
elif a == b or a == c or b == c:
    print("рівнобедрений")
else:
    print("різносторонній")
