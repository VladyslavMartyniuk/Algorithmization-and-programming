# Задача 3.10. Хвилини, тариф і ставка ПДВ мають бути невід'ємними.
minutes, price_per_minute, vat_rate = map(float, input().split())
subtotal = minutes * price_per_minute
vat = subtotal * vat_rate / 100
total = subtotal + vat

print(f"без ПДВ: {subtotal:.2f}")
print(f"ПДВ:     {vat:.2f}")
print(f"разом:   {total:.2f}")
