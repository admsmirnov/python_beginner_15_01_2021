#pep8

user_time = input("Введите время в секундах\n")
user_time = int(user_time)

hh = user_time//3600 # Count hours
print(hh , "hour")

mm = (user_time%3600)/60 # Count minutes
mm = int(mm)
print(mm , "min")

ss = user_time - (hh*3600 + mm*60 ) # Count seconds
print(ss , "sec")

timer = f"{hh}:{mm}:{ss}"
print(timer)

