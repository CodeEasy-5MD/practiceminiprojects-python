#define class
class sample:
#count as class variable
    count = 5

# define function
    def read(self):
# x as instance variable
        self.x = int(input("Enter value of x\n"))
    def display(self):
        print("Value of x =", self.x)

#create object
s1 = sample()
s2 = sample()
print("Properties for s1\n")
s1.read()
print("Value of count", + s1.count)
s1.display()

print("Properties for s2\n")
s2.read()
print("Value of count", + s2.count)
s2.display()


