from classes import Product

# Creating the products

product1 = Product("Stanley Hammer", 9.99, 5)
product2 = Product("Quartet Marker", 1.99, 4)

print('Product Data')
print(f"Product name: \t\t{product1.name}")
print(f"Product price: \t\t{product1.price}")
print(f"Discount Percent: \t{product1.discountPercent:d}%")

print(f"Discount amount: \t{product1.getDiscountAmount():.2f}")
print(f"Discount price: \t{product1.getDiscountPrice():.2f}")
