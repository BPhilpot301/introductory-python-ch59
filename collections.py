#Python collection
#a group fo data elements in python that allow us to store multiple data in a single variable

#1. Lists - They are used to store multiple items in a single variable and they use []
#Properties: Lists are ordered, changable, (or mutable) and allow duplicates

empty_list = []#this is an empty list
print(f"collection data type: {type(empty_list)}")#data type


fruits_list = ["apple", "banana","cherry","orange","grape"]
#                 0         1        2       3         4
print(f"Empty List: {empty_list}")
print(f"List: {fruits_list}")
print(f"Retreiving a value: {fruits_list[4]}")
print(f"List length: {len(fruits_list)}")
print(f"Accessing elements by Negative indexing: {fruits_list[-3]}")
#[a:b] where a is the starting index in the array (included) and b is the stopping point(not included)
print(f"Accessing elements by ranges[n:n]: {fruits_list[0:3]}")
print(f"Accessing elements by rnages[:n]: {fruits_list[:5]}")
print(f"Accessing elements by ranges[n:]: {fruits_list[1:]}")
#adding elements to the list
fruits_list.append("watermelon")
fruits_list.append("strawberry")
print(f"adding elements: {fruits_list}")
#remove elements from list
fruits_list.pop(4)
fruits_list.pop()
print(f"removing element from: {fruits_list}")
fruits_list.insert(0, "pear")
print(f"using insert method: {fruits_list}")
#fruits_list.clear()
#print(fruits_list)
fruits_list[2] = "blueberry"
print(f"changing actual values: {fruits_list}")


#2. Dictionary
#are used to store data values in key: values pairs.
#properties: ordered, changable and do not allow duplicates
my_dictionary = {
    "brand":"Ford",
    "model": "Mustang",
    "year": 1964,
    "colors":["red","white","blue","black"]
}
print(my_dictionary)
print(f"dictionary: {my_dictionary} | Type: {type(my_dictionary)}")
print(f"accessing items using keys: {my_dictionary['year']}")
print(f"dictionary length: {len(my_dictionary)}")
print(f"accessing items using get: {my_dictionary.get('colors')}")
print(f"only print the keys: {my_dictionary.keys()}")
print(f"only print the values: {my_dictionary.values()}")
#my_dictionary["year"] = 2001
#print(f"modifying the dictionary: {my_dictionary}")
my_dictionary.update({"year": 1989})
print(f"modifying the dictionary: {my_dictionary}")
my_dictionary.pop("colors")
print(f"deleting elements: {my_dictionary}")


#3. Tuples
#store multiple items in a single cariable
#properties: ordered and unchangeable
my_tuple = ("apple","cherry","banana","orange")
print(f"tuple: {my_tuple} | Data type: {type(my_tuple)}")
print(f"accessing elements: {my_tuple[2]}")
modified_tuple = list(my_tuple)
modified_tuple.append("watermelon")
modified_tuple.pop(0)
my_tuple = tuple(modified_tuple)
print(f"tuple: {my_tuple} | Data type: {type(my_tuple)}")