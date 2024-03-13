#define a list in python

cars =["Benz", "Passat", "Volvo", "Audi"]
cars.clear()
print(cars)

#removing items from list
#cars.remove("Benz")
#cars.pop(2)
#cars.pop()
#print(cars)

#Adding items to list
#cars.insert(1, "Ferrari")

#cars.append("Toyota")

others=["Vitz", "Demio"]
cars.extend(others)
print(cars)

#checking items in a list
val=input("Enter item to search for\n")
#means if item exists in cars then it tells user item exists in list
if val in cars:
    print ("item exists in the list")
else:
    print("item doesn't exist in the list")
#print in the list


#print the list

print(cars)

# display number of items in our list
print("Total items in car list:\t", len(cars))

print(cars[-1])
print(cars[:2])
print(cars[1:])

