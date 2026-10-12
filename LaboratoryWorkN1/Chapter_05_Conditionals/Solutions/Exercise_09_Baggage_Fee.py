# Тариф пропорційний кількості кілограмів перевищення.
weight_text, ticket_class = input().split()
weight = float(weight_text)
if ticket_class == "econom":
    limit = 20
elif ticket_class == "business":
    limit = 30
else:
    print("помилка класу")
    raise SystemExit
if weight < 0:
    print("помилка ваги")
else:
    fee = max(0.0, weight - limit) * 15
    print(f"{fee:g}")
