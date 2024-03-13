#WORKING AROUND THE IMMUTABILITY OF A TUPLE
mypc=("HP", "16 GB RAM", "500GB HDD", "200,000")
#Convert tuple to a list
mylist=list(mypc)
#modify the list
mylist.insert(1, "Icore 7, gen 12")
#Covert back to tuple
mypc=tuple(mylist)
print(mypc)

#CREATING A TUPLE USING VARIATON TWO:
#fruits=tuple(("Apples", "Mangoes", "Oranges", "Berries"))


#SEARCHING FOR ITEM IN TUPLE
#searchvar=input("Enter a value to search for\n")
#if searchvar in fruits:
   # print("Item exists in the tuple")
#else:
    #print("Item doesn't exist in the tuple")

#print(fruits[:-2])

#count the total items in a tuple
#print("Total items in fruits is\t" , int(len(fruits)))