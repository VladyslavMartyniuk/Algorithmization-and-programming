# Задача 3.8. Припущення: height > 0.
# ІМТ є лише розрахунковим показником, а не самостійним діагнозом.
weight, height = map(float, input().split())
bmi = weight / height ** 2

print(f"IMT = {bmi:.2f}")
