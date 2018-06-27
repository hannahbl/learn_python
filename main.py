""" Variables """

name = "Hannah"
print("Hallo", name, "!")
print(f"Hallo {name}!")
print("Hallo " + name, "!")

#

x = "Python is "
y = "awesome"
z = x + y
print(z)

#

y = 2.8  # float
z = 1j   # complex
print("y:", type(y), "z:", type(z))

""" specify a variable type"""

# casting in Python

x = float(1)
y = int(2.8888)
z = int("3")
print(x, ",", y, ",", z)

""" string """

h = "hello"
print(h[1:3])
print(len(h))

a = "Hello, World!"
print(a.upper())
print(a.replace("H", "Ja"))
print(a.split(" "), "\n")  # returns ['Hello', ' World!']


# print("Enter your name:")
# x = input()
# print("Hello, " + x)

""" lists [] -collection which is ordered and changeable """
thislist = ["apple", "banana", "cherry"]
print(thislist)
# or with constructor
thislist = list(("apple", "banana", "cherry"))
print(len(thislist))
thislist.insert(2, "raspberry")
print(thislist, "\n")

""" tuples () -collection which is ordered and unchangeable """
thistuple = ("apple", "banana", "cherry")
print(thistuple)
# or with constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple[0], "\n")

""" sets {} -collection which is unordered and unindexed """
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.remove("banana")
print(thisset, "\n")

""" dictionary { key : value} -collection which is unordered, changeable and indexed"""
thisdict = {
    "apple": "green",
    "banana": "yellow",
    "cherry": "red"
}
print(thisdict)
thisdict["apple"] = "red"
thisdict["damson"] = "purple"
print(thisdict)

# dict() constructor -keywords are not string literals  -use of equals rather than colon for the assignment
thisdict = dict(apple="green", banana="yellow", cherry="red")
del(thisdict["banana"])
print(thisdict, "\n")


""" Python conditions - if, elif, else """
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
print("\n")

""" python loops -while and for """
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
print("\n")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
      continue
  print(x)

list = [0, 1, 2, 3, 4]
for element in list:
    print(element)
print("\n")

""" range fuction"""
for x in range(6):
  print(x)

print("\n")
for x in range(3, 6):
  print(x)   # Why does it start with 3?

""" recursion """
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result
print("\n")


def easy_recursion(border):
    result = 0
    for summand in range(1, border+1):
        result = result + summand
        print(result)
    return result

def easier_recursion(border):
    result = (border * (border + 1)) / 2
    return result

print("\n Recursion Example Results : ")
tri_recursion(6)
easy_recursion(6)
easier_recursion(6)

""" lambda function """
def myfunc(n):
  return lambda i: i*n

doubler = myfunc(2)
tripler = myfunc(3)
val = 11
print("Doubled: " + str(doubler(val)) + ". Tripled: " + str(tripler(val)))
print(f"Doubled: {doubler(val)}, Tripled: {tripler(val)}")


print("\n\n")

#
# def _insert_list(value, your_list):
#     """
#     Inserts a value at the first position in a list
#     :param float value: value to be inserted
#     :param list your_list: value is inserted here
#     :return list: modified list
#     """
#     your_list.insert(2, value)
#
#     return your_list
#
#
# def create_list():
#     """
#
#     :return:
#     """
#     my_list = []
#     for i in range(0, 10):
#         my_list = _insert_list(i, my_list)
#     return my_list
#
#
# print(create_list())
#
#
# params = {
#     "name": "Hanmnah",
#     "lang": "de"
# }
#
# try:
#     params['Bla']
# except KeyError:
#     params['Bla'] = 3
# finally:
#     print(params)


