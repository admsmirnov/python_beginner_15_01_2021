"""assd = 1.2
assd = int(assd)
print(assd)
print(type(assd))"""

"""string = "abrakadbra"
str_reverse = string[::-1]
print(str_reverse)
str_reverse = string[::-2]
print(str_reverse)"""

"""string = "abrakadabra"
str_reverse = ''
symbols = list(string)
for el in range(len(string) // 2):
    tmp = symbols[el]
    symbols[el] = symbols[len(string) - el - 1]
    symbols[len(string) - el - 1] = tmp
str_reverse = ''.join(symbols)
print(str_reverse)

x = 1.1"""



"""print(True)
print(bool(20))
print(bool('text'))
print(False)
print(bool(0))
print(bool(''))
print(bool())"""

my_str = "Hello my Dear Friends"
my_list = [1, 2, 3, "hello"]

user = {
    "login": "user1",
    "password": "pswd",
    "age": 22,
}

"""for item, item2 in user.items():
    print(item, item2, sep = "----->")"""

print(my_list)
id(my_list)
id(my_list[:])
print(my_list[:])


"""for item in my_list[:]:
    print(my_list)
    id(my_list)
    id(my_list[:])
    print(my_list[:])
    my_list.append(1234)"""
