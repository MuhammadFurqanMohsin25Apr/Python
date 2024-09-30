x = input("Name: ")
y = input("Father Name: ")
z = input("Roll No.: ")
a = int(input("Total No of subjects: "))
b = int(input("Enter the total marks: "))
c = input("max marks in each subject: ")
p = 0
Grade = ("")

resultt = ""
for i in range(1, a + 1):
    name = input("subject name")
    marks = int(input("obtained marks: "))
    p += marks
    percentage = (p / b) * 100
    m = round(percentage, 2)
    t = f"{marks} out of {c} in {name}"
    resultt = t + "\n" + resultt

    if percentage >= 80 and percentage <= 100:
        Grade = "A+"
    elif percentage >= 70 and percentage <= 80:
        Grade = "A"
    elif percentage >= 60 and percentage <= 70:
        Grade = "B"
    elif percentage >= 50 and percentage <= 60:
        Grade = "C"
    elif percentage >= 40 and percentage <= 50:
        Grade = "D"
    else:
        print("You are fail")

print(f"The Subject Wise Result of {x}, son of {y}, having Roll no.: {z}, \n{resultt}\nMarks: {p} out of {b}, \nGrade: {Grade}, \nPercentage: {m}%")
