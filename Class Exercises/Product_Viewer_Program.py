from classes import Product

# Creating the products

product1 = Product("Stanley 13 Ounce Wood Hammer", 12.99, 62)
product2 = Product('National Hardware 3/4" Wire Nails' , 1.99, 30)
product3 = Product('Economy Duct Tape, 60yds, Silver', 4.99, 25)

program = True
while True:
    for i in (product1, product2, product3):
        print(i.name)

    product_number = input("Enter product Number: ")
    if product_number == '1':
        print('Product Data')
        print(f"Product name: \t\t{product1.name}")
        print(f"Product price: \t\t{product1.price}")
        print(f"Discount Percent: \t{product1.discountPercent:d}%")

        print(f"Discount amount: \t{product1.getDiscountAmount():.2f}")
        print(f"Discount price: \t{product1.getDiscountPrice():.2f}")
    elif product_number == '2':
        print('Product Data')
        print(f"Product name: \t\t{product2.name}")
        print(f"Product price: \t\t{product2.price}")
        print(f"Discount Percent: \t{product2.discountPercent:d}%")

        print(f"Discount amount: \t{product2.getDiscountAmount():.2f}")
        print(f"Discount price: \t{product2.getDiscountPrice():.2f}")
    elif product_number == '3':
        print('Product Data')
        print(f"Product name: \t\t{product3.name}")
        print(f"Product price: \t\t{product3.price}")
        print(f"Discount Percent: \t{product3.discountPercent:d}%")

        print(f"Discount amount: \t{product3.getDiscountAmount():.2f}")
        print(f"Discount price: \t{product3.getDiscountPrice():.2f}")
    else:
        print('Invalid Number')
    choice = input("View another product? (y/n): ")
    if choice == 'n':
        break



"""print('Product Data')
print(f"Product name: \t\t{product1.name}")
print(f"Product price: \t\t{product1.price}")
print(f"Discount Percent: \t{product1.discountPercent:d}%")

print(f"Discount amount: \t{product1.getDiscountAmount():.2f}")
print(f"Discount price: \t{product1.getDiscountPrice():.2f}")"""