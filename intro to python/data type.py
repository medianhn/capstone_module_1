import math
# Data Type
# Input Variable

this_string = "This is String"
this_integer = 123*10**6
this_integer2 = 122/3
this_integer3 = 122//3
this_boolean = False
this_list = ["apple", "banana", "cherry"]
this_tuple = ("apple", "banana", "cherry")
this_set = {"apple", "banana", "cherry"}
this_dictionary = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_string_datatype = type(str(this_integer))
print(this_string_datatype)
print(this_integer3)
print(math.fabs(173.46))
print(str(this_integer) + " is an integer")
txt = "{} is a list"
print(txt.format(this_list))


# Show your data type in Terminal/Console
print(this_string, "is a string")
print(this_integer, "is an integer")
print(this_boolean, "is a boolean")
print(this_list, " is a list")
print(this_tuple, " is a tuple")
print(this_set, " is a set")
print(this_dictionary, " is a dictionary")