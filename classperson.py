#define class
class person:

#define read function
    def Read(self):
        self.name = input("Enter person name\n")
        self.weight = input("Enter person weight\n")
        self.age = input("Enter person age\n")
        self.height = input("Enter person height\n")
        self.gender = input("Enter person gender\n")

#define write function.
# Work of write function is to display class variables
    def Write(self):
        print(self.name, self.weight, self.height, self.age, self.gender)

#create object (of class person)
P = person()
P1 = person()

# call read and write methods respectively
P.Read()

P.Write()
print("Object 1\n")

P1.Read()

P1.Write()
print("Object 2\n")



