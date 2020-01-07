# coding=UTF-8


#########################################################################################
#8 函数
#8.1 定义函数
def greet_user():
    """ 显示简单的问候语 """
    print("Hello!")
greet_user()


#8.1.1 向函数传递参数
def greet_user(user_name): #user_name是一个形参
    """ 显示简单的问候语 """
    print("Hello, " + user_name.title() + "!")
greet_user("myra") #"myra"是一个实参


#8.2 传递实参
#8.2.1 位置实参
#函数调用中实参的顺序必须与函数定义中形参的顺序一致
def describe_pet(animal_type, pet_name):
    """ 显示宠物的信息 """
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet("dog", "hachiko")


#8.2.2 关键字实参
#无需考虑函数调用中实参的顺序
#务必准确地指定函数定义中形参名
def describe_pet(animal_type, pet_name):
    """ 显示宠物的信息 """
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name = "hachiko", animal_type = "dog")


#8.2.3 默认值
#8.2.4 等效的函数调用
#8.2.5 避免实参错误


#8.3 返回值









#########################################################################################
