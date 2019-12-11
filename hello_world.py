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
print(message.title())
print(message.upper())
print(message.lower())#FFFFFF

#tab and enter
print("\n\t" + message.title() + "\n\t" + message.upper() + "\n\t" + message.lower())
message = " Deng Meiyan  \t"

#trim and connect
print(message.rstrip() + "End")
print(message.lstrip() + "End")
print(message.strip() + "End")

#Calculate
print(3+2)
print(3-2)
print(3*2)
print(3/2)
print(3**2) #2 to the power of 3


print(0.3+0.2)
print(3*0.2)

#int convert to string
age = 37
message = "Happy " + str(age) + "th birthday!"
print(message)
######################################################################



######################################################################
#arrayList index is from 0. arrayList[index]
colors = ["black", "white", "yellow", "blue", "red", "green"]
print(colors)
print(colors[3].title())

#arrayList last one
print(colors[-1])
print(colors[-3])

#arrayList modify
colors[3] = "purple"
print(colors)

#arrayList append(value)
colors.append("blue")
print(colors)

#arrayList insert(index, value)
colors.insert(2, "orange")
print(colors)


#arrayList delete:del arrayList[index]
del colors[2]
print(colors)


#arrayList delete:pop(index)
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
print(min(squares))
print(max(squares))
print(sum(squares))

# loop can also be simply coded like this:
squares = [value**2 for value in range(1, 11)]
print(squares)

cubes = [value**2 for value in range(1, 11)]
print(cubes)


#part of arrayList
orders = ["0", "1", "2", "3", "4", "5", "6", "7"]
print(orders[1:3])
print(orders[:3])
print(orders[3:])
print(orders[-3:])

#loop in the part of arrayList
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


########################################################################
#if...else...
cars = ['toyota','audi','honda','bmw']
for car in cars:
    if car.lower() == "bmw":
        print(car.upper())
    else:
        print(car.title())









##########################################################################
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

