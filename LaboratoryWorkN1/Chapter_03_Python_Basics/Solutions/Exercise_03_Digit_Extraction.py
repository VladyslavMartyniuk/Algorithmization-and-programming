# Задача 3.3. На вході — ціле трицифрове число від 100 до 999.
n = int(input())
hundreds = n // 100
tens = n // 10 % 10
units = n % 10

digit_sum = hundreds + tens + units
print(f"{hundreds} {tens} {units}, сума = {digit_sum}")
