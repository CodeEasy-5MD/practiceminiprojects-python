#defining dictionary
products={"Code": "P001", "Name": "Laptop", "Price": 125000.00, "Quantity": 2, "ExpiryDate": "30-10-2027"}
print(products)

#to access keys
print(products["Price"])
#gets value for code key
print(products.get("Code"))
#get all the keys
print(products.keys())
#get all the values
print(products.values())
#get keys and values
print(products.items())

#adding new item
products["ReorderLevel"] = 3

#changing/updating item
products["Price"] = 120000.00
products.update({"Quantity": 10})

#removing items
#1.pop()
products.pop("Price")
#2.delete keyword
del products["Quantity"]
#3.popitem() to remove last item
products.popitem()
print(products)
