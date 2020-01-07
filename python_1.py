# coding=UTF-8

#from hashids import Hashids


######################################################################
#String: "" or '' is ok!
message = "Hello Python world!"
print(message)
message = 'Hello Python world!'
print(message)
message = 'Hello "Python" world!'
print(message)
message = "Hello 'Python' world!"
print(message)

#String case change
#字符串大小写切换
print(message.title())
print(message.upper())
print(message.lower())#FFFFFF

#tab and enter
print("\n\t" + message.title() + "\n\t" + message.upper() + "\n\t" + message.lower())
message = " Deng Meiyan  \t"

#trim and connect
#去空格，字符串拼接
print(message.rstrip() + "End")
print(message.lstrip() + "End")
print(message.strip() + "End")

#Calculate
#计算
print(3+2)
print(3-2)
print(3*2)
print(3/2)
print(3**2) #3的2次方


print(0.3+0.2)
print(3*0.2)

#字符串转换
age = 37
message = "Happy " + str(age) + "th birthday!"
print(message)
######################################################################



######################################################################
#arrayList index is from 0. arrayList[index]
#列表下标从0开始
colors = ["black", "white", "yellow", "blue", "red", "green"]
print(colors)
print(colors[3].title())

#arrayList last one
print(colors[-1])
print(colors[-3])

#arrayList modify
#列表元素编辑
colors[3] = "purple"
print(colors)

#arrayList append(value)
#列表元素追加
colors.append("blue")
print(colors)

#arrayList insert(index, value)
#列表元素插入
colors.insert(2, "orange")
print(colors)


#arrayList delete:del arrayList[index]
#列表元素删除
del colors[2]
print(colors)


#arrayList delete:pop(index)
#列表元素删除
#pop(): delete the last one
#pop(index): delete the one of index
color_pop = colors.pop(2)
print(color_pop)
print(colors)

#The different with del and pop:
#del: the element that was deleted can't be used any more.
#pop: the element that was poped can be saved into a variation.


#arrayList remove(value): remove the first one that equals to the value
color_remove = "red"
colors.remove(color_remove)
print(colors)
colors.append(color_remove)
print(colors)


######################################################################
#arrayList sort: change the order forever
colors.sort()
print(colors)

#arrayList sort(reverse=True): change the order reversely forever
colors.sort(reverse=True)
print(colors)

#arrayList sorted: change the order temporarily
print(sorted(colors))
print(colors)
colors.sort()
print(colors)

#arrayList sorted(reverse=True): change the order reversely temporarily
print(sorted(colors))
print(sorted(colors, reverse=True))
print(colors)


#arrayList.reverse()
chars = ['b','a','e','d','c']
chars.reverse()
print(chars)


#len(arrayList): return the length of the arrayList
print(len(chars))


######################################################################
#loop: indent is very important! (4 space, not tab)
#loop: Don't forget ":"
for color in colors:
    print(color)

print(color)


#range
#print 1~4
for value in range(1, 5):
    print(value)

print(range(1, 5))  #range(1, 5)

#range to list
numbers = list(range(1,6))
print(numbers)  #[1, 2, 3, 4, 5]


even_numbers = list(range(2,11,2))
print(even_numbers) #[2, 4, 6, 8, 10]


squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)  #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


#min, max, sum of the range
#求最大最小值，合計值
print(min(squares))
print(max(squares))
print(sum(squares))

# loop can also be simply coded like this:
#列表解析
squares = [value**2 for value in range(1, 11)]
print(squares)

cubes = [value**2 for value in range(1, 11)]
print(cubes)


#part of arrayList
#列表切片
orders = ["0", "1", "2", "3", "4", "5", "6", "7"]
print(orders[1:3])
print(orders[:3])
print(orders[3:])
print(orders[-3:])

#loop in the part of arrayList
#遍历列表切片
for order in orders[-3:]:
    print(order)


#copy list
#复制列表
my_foods = ['pizza', 'falefel', 'cake']
friend_foods = my_foods[:]
# wrong: friend_foods = my_foods !!!!!!!!Caution!!!!!!!!
my_foods.append('ice')
friend_foods.append('coffee')

print(my_foods)
print(friend_foods)


#simple list that can't be modified (but can be revalued)
#元组：不可变的列表
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# wrong: dimensions[0] = 400

#元组遍历
for dimension in dimensions:
    print(dimension)

#不可修改元组的元素，但可以重新定义整个元组（重新给元组变量赋值）
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)


########################################################################
#if-else语句
cars = ['toyota','audi','honda','bmw']
for car in cars:
    #转换成小写再比较
    if car.lower() == "bmw":
        print(car.upper())
    else:
        print(car.title())

#检查字符串是否相等用==
#检查字符串是否不相等用!=
#比较数值：==,<,<=,>,>=
#使用and/or检查多个条件


#检查特定值是否包含在列表中：in/not in
banned_users = ["andrew", "carolina", "david"]
user = "marie"
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")


car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("Is car == 'audi'? I predict False.")
print(car == 'audi')


#if-elif-else语句
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("\nYour admission cost is $" + str(price) + ".")

#判断列表是否为空
#将列表名用于条件表达式中，包含元素时返回True，不包含元素时返回False
empty_list = []
if empty_list:
    print("列表不为空")
else:
    print("列表为空")


#########################################################################################
#6 字典

#创建一个空字典
alien = {}
print(alien)


#访问字典中的值
alien = {'color': 'green', 'points': 5}
print(alien)
print(alien['color'])
print(alien['points'])


#增加键值对
alien['X_position'] = 0
alien['Y_position'] = 25
print(alien)
print(alien['X_position'])
print(alien['Y_position'])


#修改字典中的值
print("The alien is " + alien['color'] + ".")
alien['color'] = 'yellow'
print("The alien is now " + alien['color'] + ".")


#删除键值对
alien = {'color': 'green', 'points': 5}
print(alien)
del alien['points']
print(alien)


#由类似对象组成的字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'java',
    'myra': 'python',
    }

print("Phil's favorite language is " +
    favorite_languages['phil'].title() +
    ".")


#6.3 遍历字典 
#6.3.1 遍历所有的键值对：dictionary.items()
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")


#6.3.2 遍历字典中所有的键：dictionary.keys()
#遍历字典时，默认遍历所有的键，所以.keys()可以省略
#不省略.keys()
for name in favorite_languages.keys():
    print(name.title())
#省略.keys()
for name in favorite_languages:
    print(name.title())


#6.3.3 按顺序遍历字典中所有的键
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")


#6.3.4 遍历字典中所有的值：dictionary.values()
for language in favorite_languages.values():
    print(language.title())

#去掉重复的值：用集合set()来提取
#集合类似于列表，但每个元素都是独一无二的
for language in set(favorite_languages.values()):
    print(language.title())


#6.4 嵌套
#6.4.1 字典列表
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': '5', 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == "green":
        alien['color'] = "yellow"
        alien['points'] = "10"
        alien['speed'] = "medium"
for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))


#6.4.2 在字典中存储列表
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'java'],
    'myra': ['java', '.net'],
    }
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print("\n" + name.title() + "'s favorite languages is " + languages[0])
    elif len(languages) > 1:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())


#6.4.3 在字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())



#########################################################################################
#7 用户输入和While循环
#7.1 函数input()的工作原理
#7.1.1 使用input()获取文本输入
message = "\nIf you tel us who you are, we can personalize the messages you see."
message += "\nWhat is your first name? "
name = input(message)
print("Hello, " + name.title() + "!")


#7.1.2 使用int()获取数值输入
height = input("\nHow tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("You're tall enough to ride!")
else:
    print("You'll be able to ride when you're a little older.")


#7.1.3 求模运算符（返回余数）
number = input("\nEnter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("The number " + str(number) + " is even.")
else:
    print("The number " + str(number) + " is odd.")


#7.2 while循环简介
#7.2.1 使用while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


#7.2.2 让用户选择何时退出
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)


#7.2.3 使用标志Flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
active = True
while active:
    message = input(prompt)
    if message != 'quit':
        print(message)
    else:
        active= False


#7.2.4 使用break退出循环：不再执行余下的代码，并退出整个循环
prompt = "\nPlease enter the name of a city you hav visited:"
prompt += "\nEnter 'quit' when you are finished." 
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")


#7.2.5 在循环中使用continue:不再执行循环内余下的代码，并返回到循环的开头
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    else:
        print(current_number)


#7.2.6 避免无限循环
#结束无限循环，可以按Ctrl+C
# i = 1
# while i < 2:
#     print(i)



#7.3 使用while循环处理列表和字典
#7.3.1 在列表之间移动元素
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop() #pop()：删除列表中的最后一个元素
    print("Verifying user: " + current_user)
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user)

#7.3.2 删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)


#7.3.3 使用用户输入来填充字典
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat's your name?")
    response = input("Which mountain would you like to climb someday?")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == "no":
        polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name.title() + " would like to climb " + response.title() + ".")





#########################################################################################
#hex
print("\n")
hex_1 = bytes.fromhex("abcd")
print(hex_1)
print(hex_1.hex())
print(hex_1)


#indent:Ctrl+I,Ctrl+U
#comment:Ctrl+E

#import this

#hashids = Hashids()
#hash_1 = hashids.encode(hex_1)
#print('Hash: ' + hash_1)

