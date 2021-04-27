#

# my_income = 300000
# my_taxrate= 0.1
# my_tax = my_income * my_taxrate

# print(my_tax)


# myString = "Kuntal Ghosal"

# print(myString [::2])
# x = myString.split()
# print(x)

# x = "National Animal: {} National Flower: {}".format("Tiger", "Lotus")

# x = "National Animal: {a} National Flower: {b}".format(a="Tiger", b="Lotus")
# print(x)


# Python List


# myList = ["avsvv", 1, 2, 3, 4, 5, 6]

# listTwo = [44, 55, 22, 11]

# myList.extend(listTwo)

# print(len(myList))
# print(myList[0])
# print(myList[1:4])
# print(myList[::2])

# This is replace the item with his given position

# myList[1] = "Kuntal"

# append add item from end

# myList.append("Hello")
# print(myList)

# Pop function by default delete the item from the last and also delete the item of given index number

# a = [1, 2, 3, 6, 5, 4]
# b = ["a", "g", "f", "y", " f"]

# a.pop(2)
# a.pop()
# a.reverse()
# a.sort()
# print(b)


# Nested List

# a = [1, 2, 3, 4, [9, [8, 7], 6]]

# b = a[4][1][1]
# print(b)


# List Matrix Problem

# LIST COMPREHENSION

# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# b = "Comprehension"
# c = b.upper()
# b = [row[0] for row in a]
# b = [row[1] for row in a]
# b = [row[2] for row in a]


# print(c)


# **** Dictionaries in Python ***


# a = {"key1": 123, "key2": 456, "key3": {"c": 2, "d": 5, "e": 10}}
# f = a["key3"]["d"]
# a["key3"]["d"] = "Hello"
# a["key3"]["Best Footballer"] = "MESSI"
# print(a)


# TUPLES======>>>>>>

# a = (1, "fff", True)
# print(a[1].upper())

# notes: a[1] = 4 we can't In list we can change aur add value


# SET:=> set is little bit similar to pytho dictionaries,it takes unique value and delete the repeted values.

# b = set()
# b.add(8)
# b.add(5)
# b.add(5)
# b.add(2)
# b.add(2)
# b.add(1)

# print(b)

# converted = set([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 7, 7, 7, 8, 8, 8])
# print(converted)


# OPERATORS

# a = 1 == "1"
# a = 0.1 <= 1

# AND and OR operator===>>>

# a = (2 == 2) and (1 < 2)
# a = (2 < 1) or (2 > 1)
# print(a)

# IF ELSE

# if 1 > 4:
#     print("HELLO")
# elif 2 > 4:
#     print("KUNTAL")
# else:
#     print("Error!")


# FOR LOOP ===>>>


# a = [1, 2, 3, 4, 5, 6]

# for i in a:
#     print(i)


# a = {
#     "b": "FOCUS on your study",
#     "c": "Get a great job",
#     "a": "Stay high always",
# }


# for item in a:
#     print(a[item])
#     print(item)


# ***


# a = [(1, 2), (3, 4), (5, 6)]

# for (tup1, tup2) in a:
#     print(tup1)
#     print(tup2)


# Whilw LOOP ===>>>


# i = 1

# while i <= 5:
#     print("i is: {}".format(i))
#     i = i + 1


# RANGE====>>
# third param is for print 0 to 30 after 4 digit
# a = list(range(0, 30, 4))

# print(a)


# for item in range(0, 18):
#     print(item)

# APPEND

# x = [1, 2, 3, 4, 5]
# y = []
# for item in x:
#     y.append(item ** 3)
#       print(y)


# out = [num ** 2 for num in x]

# print(out)


# print(y)


# *** FUNCTIONS ***#


# def my_name(name="KUNTAL"):
#     print(name)


# my_name("Ghosal")
