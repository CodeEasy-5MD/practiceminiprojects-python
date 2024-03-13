x = float(input("Enter cat marks:\n"))
y = float(input("Enter exam marks:\n"))

score = (x+y)

if score < 50:
    print("sudent has failed")
elif score == 50:
    print("Student has just made it")
else:
    print("Student has passed")

