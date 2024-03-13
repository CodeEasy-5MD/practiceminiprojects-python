#defining global variables
lecname = ""
unit_name= ""
unit_code = ""

#define program function
def scheduler():
    lecture_hall = input("Enter lecture hall\n")
    time = input("Enter the time\n")
    day = input("Enter the day\n")

#if/decision statements
    if lecture_hall == "TH" and time == "8:00-11:00" and day == "Monday":
        lecname = "Joe"
        unit_name= "Database Systems"
        unit_code = "CMT 110"
        flag = 1
    elif lecture_hall == "OH" and time == "2:00-5:00" and day == "Friday":
        lecname = "Christiano"
        unit_name= "Communication Skills"
        unit_code = "CMT 200"
        flag = 1
    else:
        flag = 0

    if flag == 1:
        print(lecname, unit_name, unit_code)
    elif flag == 0:
        print("Hall free at that time\n")

#call function
scheduler()
