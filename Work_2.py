#  Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def keyparametry (*, name, famaly, phone_number, adress, RAL ):
    param = {name:"name", famaly:"famaly", phone_number:"phone_number", adress:"adress", RAL:'RAL'}
    print (param)
    print(type(param))

keyparametry (RAL=True, name="John", famaly="Smith", phone_number=322223, adress="Black_Karackatiza")

print("-" * 40)

MyDictionary = {}
def keyparametry1 (**kwargs ):
    for key, value in kwargs.items():
        MyDictionary[value] = key

keyparametry1 (RAL=True, name="John", famaly="Smith", phone_number=322223, adress="Black_Karackatiza")
print(MyDictionary)
print(type(MyDictionary))