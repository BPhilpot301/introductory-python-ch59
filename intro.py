print("Hello world from Python!")
print(2)
print(5*3)
print(True)

#this is how you comment


# creating variable
name = "Britney"
age = 35
middle_name = "Lynn"
last_name = "Philpot"
found = "False"
print(name)

#concatenation
print("My name is: " + name + ", and I'm " + str(age) + " years old.")
print("Did he show up to the class?" + str(found))


#the f format
#f"" or f"""""

print(f"My name is: {name}, and I'm {age} years old!")

#the type() function helps us to know the data type of the variable
print(type(name))
print(type(age))
print(type(True))

#casting
#helps us convert different data types
#str() - convert from and data type to string
#int() - convert string number to numeric values
#float() - convert string number to Float type
print(20+int("20"))
print(20+age)
print(20+int(2.98))
print(20+float(2.98))


#input method
#is going to allow us to interact with the terminal and pass some values

#print(type(input("Enter your age here: ")))
#print(type(input("Enter your name here: ")))
#new_age = int(input("Enter a new age: "))
#print(age + new_age)

x = int(input("Enter a first value: "))
y = int(input("Enter a second value: "))
print(x+y)