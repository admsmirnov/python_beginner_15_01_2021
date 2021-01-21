
"""int
float
str"""

my_int = 555
my_float = 666.777
my_str = "Моя строка"
my_str_1 = "567"

print("Enter your age") #проверка возраста
age = input()
print("Correct, you are", age)

print(type(age))
age = int(age)
print(type(age))
print(my_int, my_float, my_str)
my_str_1 = int(my_str_1)
my_summ = (my_str_1 + my_int) * my_float * age
print(my_summ)



