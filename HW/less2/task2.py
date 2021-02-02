#PEP8

user_answer = input("Введите список через запятую\n")
print(user_answer)
user_list = user_answer.split(",")
print(user_list)

idx = 0

while idx < len(user_list[:-1]):
    user_list[idx], user_list[idx + 1] = user_list[idx + 1], user_list[idx]
    idx += 2
print(user_list)


