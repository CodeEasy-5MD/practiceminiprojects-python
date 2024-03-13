#define function marks and return
def marks (a , b):
    return a+b
#enter values from keyboard
a = int(input("Enter cat marks\n"))
b = int(input("Enter exam marks\n"))

#assign variable to summation operation
x=marks(a, b)

#if elif else statement to make decision
if x >= 50:
   print("Pass")
elif x < 50:
    print("Fail")
else:
    print("No Marks")


