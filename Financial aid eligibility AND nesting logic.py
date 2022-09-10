#The reason for nesting is when we have to evaluate for logics AND, OR
#Student elegibe for Financial Aid if he/she meets all 5 criterias.
#Yes for citizenship or permenant resident
#Wages are less than 50k from previous year
#Enrolled in 12 credit hours or more in the current semester
#Total GPA is greater than or equal to 2.0
#Attendance average is greater than or equal to 95
citizenship = input("Enter Yes or No if you are a US citizen or permenant resident: ")
wages = int(input("Enter total wage from your income tax last year: "))
credit_hours = int(input("Enter total credit hours you are taking this semester: "))
gpa = float(input("Enter current transcript total GPA: "))
attendance = int(input("Enter average attendance: "))
citizenship_strip = citizenship.strip().lower()
if citizenship_strip == "yes":
    if wages < 50000:
        if gpa >= 2:
            if credit_hours >= 12:
                if attendance >= 95:
                    print("You are eligible for Financial Aid")
                else: 
                    print("Not eligible, attendance is less than 95.")
            else:
                print("Not eligible, you are enrolled in less than 12 credit hours.")
        else:
            print("Not eligible, Transcript GPA is less than 2.0") 
    else:
        print("Not eligible, wages are greater than 50k.")
else:
    print("Not eligible, Not a US citizen or permenant resident.")