x, y = map(float, input().split())
if x == 0 and y == 0:
    print("початок")
elif x == 0:
    print("на осі OY")
elif y == 0:
    print("на осі OX")
elif x > 0 and y > 0:
    print("I")
elif x < 0 and y > 0:
    print("II")
elif x < 0 and y < 0:
    print("III")
else:
    print("IV")
