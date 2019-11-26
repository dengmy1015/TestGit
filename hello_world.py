#from hashids import Hashids

#String
message = "Hello Python world!"
print(message)
message = 'Hello Python world!'
print(message)
message = 'Hello "Python" world!'
print(message)
message = "Hello 'Python' world!"
print(message)

#
print(message.title())
print(message.upper())
print(message.lower())
print("\n\t" + message.title() + "\n\t" + message.upper() + "\n\t" + message.lower())
message = " Deng Meiyan  \t"

#trim
print(message.rstrip() + "End")
print(message.lstrip() + "End")
print(message.strip() + "End")

#keisan
print(3+2)
print(3-2)
print(3*2)
print(3/2)
print(3**2)


print(0.3+0.2)
print(3*0.2)

#int to string
age = 37
message = "Happy " + str(age) + "th birthday!"
print(message)

#array
colors = ["black", "white", "yellow", "blue", "red", "green"]
print(colors)
print(colors[3].title())

#array last one
print(colors[-1])
print(colors[-3])

#array modify
colors[3] = "purple"
print(colors)

#array append(value)
colors.append("blue")
print(colors)

#array insert(index, value)
colors.insert(2, "orange")
print(colors)


#array delete.del
del colors[2]
print(colors)


#array delete.pop(index)
color_pop = colors.pop(2)
print(color_pop)
print(colors)


#array remove(value)
color_remove = "red"
colors.remove(color_remove)
print(colors)
colors.append(color_remove)
print(colors)

#array sort
colors.sort()
print(colors)

colors.sort(reverse=True)
print(colors)

#array sorted
print(sorted(colors))
print(colors)
colors.sort()
print(colors)
print(sorted(colors, reverse=True))
print(colors)


#array reverse
chars = ['b','a','e','d','c']
chars.reverse()
print(chars)


#array len()
print(len(chars))

#loop: indent is very important! (4 space, not tab)
#loop: Don't forget ":"
for color in colors:
    print(color)

print(color)


#range
for value in range(1, 5):
    print(value)

print(range(1, 5))  #range(1, 5)

#range to list
numbers = list(range(1,6))
print(numbers)  #[1, 2, 3, 4, 5]


even_numbers = list(range(2,11,2))
print(even_numbers) #[2, 4, 6, 8, 18]


squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)


#min, max, sum of the range
print(min(squares))
print(max(squares))
print(sum(squares))


squares = [value**3 for value in range(1, 11)]
print(squares)


#part of list
orders = ["0", "1", "2", "3", "4", "5", "6", "7"]
print(orders[1:3])
print(orders[:3])
print(orders[3:])
print(orders[-3:])

for order in orders[-3:]:
    print(order)


#copy list
my_foods = ['pizza', 'falefel', 'cake']
friend_foods = my_foods[:]
# wrong: friend_foods = my_foods
my_foods.append('ice')
friend_foods.append('coffee')

print(my_foods)
print(friend_foods)


#simple list that can't be modified (but can be revalued)
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# wrong: dimensions[0] = 400
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)


#if...else...
cars = ['toyota','audi','honda','bmw']
for car in cars:
    if car.lower() == "bmw":
        print(car.upper())
    else:
        print(car.title())




#hex
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

