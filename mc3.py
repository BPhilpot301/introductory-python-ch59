#create the function
def validation(a,b):
    #if-else statements
    if a == b:
        print("They're the same")
    else:
        print("They're different")

#declaring variable and using the input function
a = int(input("Enter the first value"))
b = int(input("Enter the second value"))

#calling the function
validation(a,b)