#PEP8

print("."*60)
while True:
    user_num = input("Введите целое положительное число\n")
    if user_num.isdigit():
        user_num = int(user_num)
        break
        print("Ошибка ввода, это не целое положительное число")

result = 0
while user_num and result != 9:
    tmp = user_num % 10
    if tmp > result:
        result = tmp
    user_num //= 10
print(result)
