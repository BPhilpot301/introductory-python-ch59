#For loop
#is used for iterating over a sequence (list, tuples, dictionaries, set, strings)
#keywords: continue jumps to the next iteration and break finishes the for loop

fruits_list = ["apple", "banana","cherry","orange","grape"]

    

    
my_dictionary = {
    "brand":"Ford",
    "model": "Mustang",
    "year": 1964,
    "colors":["red","white","blue","black"]
}   

for fruit in fruits_list:
    if fruit == "cherry":
        #break
        continue

    print(fruit)

print("-----------")

for items in my_dictionary:
    print(f"keys only: {items} | retrieving  the value: {my_dictionary[items]}")

for x in "iteration":
    print(x)

print("------------")

#range(start_value, stop_value, steps or increments)
for number in range(0,len(fruits_list),2):
    print(fruits_list[number])

