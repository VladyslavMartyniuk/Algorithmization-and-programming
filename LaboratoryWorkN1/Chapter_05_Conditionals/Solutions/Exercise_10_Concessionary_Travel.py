age_text, sex = input().split()
age = int(age_text)
if age < 0:
    print("помилка віку")
elif sex not in ("ч", "ж"):
    print("помилка статі")
elif age < 18 or (sex == "ж" and age >= 60) or (sex == "ч" and age >= 65):
    print("так")
else:
    print("ні")
