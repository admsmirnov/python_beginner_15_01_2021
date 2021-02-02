#PEP8

time = ["зима", "зима", "весна", "весна", "весна", "лето", "лето", "лето", "осень", "осень", "осень", "зима"]


while True:
    month = input("Введи номер месяца\n")
    if month.isdigit():
        month = int(month)
        break
        print("Введите число")

print(time[month - 1])
