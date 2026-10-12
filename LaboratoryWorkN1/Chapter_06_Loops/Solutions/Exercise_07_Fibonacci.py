n = int(input())  # кількість членів послідовності, n >= 1
first, second = 0, 1
total = 0
numbers_for_output = []  # список використано лише для рядка виводу
for _ in range(n):
    numbers_for_output.append(str(first))
    total += first
    first, second = second, first + second
print(" ".join(numbers_for_output) + f", сума = {total}")
