x = float(input("Enter cat marks:\n"))
y = float(input("Enter exam marks:\n"))

score = (x+y)

if score >= 70 && <= 80:
    print('A')
elif score >= 60 && <= 69:
    print('B')
elif score >= 50 && <=59:
    print('D')
else:
    print('student did not attend semester')