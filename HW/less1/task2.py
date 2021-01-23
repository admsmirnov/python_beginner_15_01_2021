#pep8

while True:
    user_time = input("Введите время в секундах\n")
    if user_time.isdigit():
        user_time = int(user_time)
        break
    print("Ошибка ввода, это не число")

"""user_time = input("Введите время в секундах\n")
user_time = int(user_time)"""

hh = user_time // 3600 # Count hours
print(hh , "hour")

mm = (user_time % 3600)/60 # Count minutes
mm = int(mm)
print(mm , "min")

ss = (user_time % 3600)%60 # Count seconds
print(ss , "sec")

timer = f"{hh:>02}:{mm:>02}:{ss:>02}"
print(timer)

