#if else statements
#execute some logic or instructions if (and only IF) the condition is correct
#we can catch with an else in case that the conditon doesnt match

#equals: a == b
#not equals: a!= b
#less than: a < b
#greater than: a> b
#less than or equal to: a <= b
#greater than or equal to: a >= b

age = 101

if age < 100:
    if age < 21:
        print("You're a minor without access!")
    else:
        print("You're younger than a 100 year old!")
elif age==100:
    print("Congratulations, you got to live a century!")
else:
    print("I'm sorry you are getting old!")

x = 5
y = 8
if x > y:
    print("Hello")
else:
    print("welcome")

#create a python file that compares two values by passing them in the terminal. If both values are the same print the message "Theyre the same", if not print another message that says "theyre different"
