score = int(input())
if score < 0 or score > 100:
    print("помилка")
elif score >= 90:
    print("A")
elif score >= 82:
    print("B")
elif score >= 74:
    print("C")
elif score >= 64:
    print("D")
elif score >= 60:
    print("E")
elif score >= 35:
    print("FX")
else:
    print("F")
