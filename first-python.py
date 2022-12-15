# here is a comment

# snake_case <- convention for naming variables
total_apples = 7


#python's console.log
# print(total_apples) #prints to the terminal

########## Datatypes!

# type()
# type(42)
# print(type(42))
# print(type(42.11))
# print(type('hi there'))
# print(type("ayoooooo"))
# print(type([]), "< []")
# print(type({}), "<- {}")
# print(type(True), "True")
# print(type(False), "False")

# since everything comes from a class, EVERYTHING IN PYTHON IS AN OBJECT

# Object - properties(values), methods(functions)

# to look inside a datatype to find its methods
# dir()
# print(dir([]))

#python doesnt have null
# print(type(None))

# % modulo gives us the remainder
# if 4 % 2 == 0:
#     print('even')
# else:
#     print('odd')

phones = 2
# print("I got " + str(phones) + " phones")

gold_rings = 8

# print(str(gold_rings) + " gold rings like I'm sha shabba ranks")




## allows you to not write a conversion method. You can inject into 'f' string with {}
msg = f"i got {phones} phones"
# print(msg)

# print(dir(msg))

# print(msg.split(' '))

# print(len(msg))

is21 = 21 or 'not'

# print(is21)

floor = "sticky"
walls = "clean"

# below is a function denoted by ":" and indentation.
if floor == "sticky":
    print('clean the floor')
elif walls == 'clean':