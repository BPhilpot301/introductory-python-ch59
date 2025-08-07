#mini challenge 4
#calculate the total of a product cart list and also calculate the average of the product cart.

product_cart = [100,200,300,400,500]




#create a function called totalthat receives a list as a parameter and return the total value
def get_total(cart):
    total=0
    for product in product_cart: #100
        total=total+product #0=0+100=100
    return total
print(get_total(product_cart))
#create an average function that receives two parameters: total and return the average value
def get_average(total,count):

    return total/count
total = get_total(product_cart)
avg = get_average(total, len(product_cart))



#print the total and average variables using a f format that says: "the total is: " and "The average is: "
print(f"The total is: {total}")
print(f"The average is: {avg}")