#TASK 1
'''
print("Hello", end="\t")
print("world")

a=5
b=0
#print(a/b)

#print(val)

c = 20
d = "hello"
e = "world"
DE = d + e
print(DE + str(c))

for i in range (10000000):
    print("67")
'''



#Task 2
'''
try:
    print("Start of the program")
    print("name" + 210)
    print(val)
    print(10/0)
except (ZeroDivisionError, NameError, TypeError):
    print("division by zero or name error")
except TypeError:
    print("TYPE ERROR!")

print("some more code")
print("end code")
'''

#tASK 3
'''
try:
    print("Hello")
    print(val)
except NameError:
    print("NameError")
else:
    print("I DUNNO THIS ERROR MAN")
finally:
    print("I just exist")
'''
'''
#Task 4
def checker(val):
    if type(val) != str:
        raise TypeError("val is not a string")
    else:
        print("HELLO"+val)

checker("67")
'''
'''
#Task 5
class BuildingError(Exception):
    def __str__(self):
        return f"Building error. The house can't be built!"
def check_material(material, limit):
    if material >= limit:
        print("OK")
    else:
        raise BuildingError(material)
check_material(2,5)
'''

#task 6



























