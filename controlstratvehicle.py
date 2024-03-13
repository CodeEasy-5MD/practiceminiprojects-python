# values the program accepts
time = input("Enter time for travel\n")
destination = input("Enter destination for travel\n")

#decisions within program
if time == "10:00" and destination == "Voi":
    vregno = "KDZ 201"
    atime = "5:00 pm"
    fare = 2000.00
    flag = 1
elif time == "2:00" and destination == "Kisumu":
    vregno = "KAT 221V"
    atime = "11:00 PM"
    fare = 5000.00
    flag = 1
else:
    flag = 0

# determine value of flag
if flag==1:
    print("Bus found!\n")
    print(vregno, atime, fare)
if flag==0:
    print("Sorry, No bus match the two criteria!\n")

