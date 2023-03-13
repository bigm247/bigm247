print("Hello, Michael")
print("Humpty Dumpty sat on a wall,")
print("Humpty Dumpty had a great fall.")
print("All the king's horses and all the king's men")
print("couldn't put Humpty together again")
print("Hello, Imola!")
print("Hello, Deen!")
print("Hello, Richard!")
print("Michael")
print(31)
print(1.82)
print(13 + 22)
print(13 - 22)
print(22 * 13)
print(22 / 13)
print(22 // 13)
print(22 % 13)
daily_coding_hours = 6
semester_week = 17
working_days = 5
total_coding_hours_in_semester = daily_coding_hours * semester_week * working_days
print("Total working hours per semeter:", total_coding_hours_in_semester)
if_average_work_hours = 52
total_average_hours = if_average_work_hours * semester_week
coding_percentage_hours = total_coding_hours_in_semester / total_average_hours * 100
print("Coding percentage if aveerage working hours is 52:",coding_percentage_hours)
my_favorite_number = 10
print("My favorite number:" + str(10))
a = 123
b = 526
a,b = b, a
print(a)
print(b)
massInKg = 81.2
heightInm = 1.78
BMI = massInKg / (heightInm ** 2)
print("Body mass Index:", BMI)
My_name = "Michael Oladele"
My_age = 31
My_height = 1.82
Married = False
print("My Name is:", My_name)
print("My age:", My_age)
print("My Height:", My_height)
print("Married:", Married)
a = 3
a +=10
print(a)
b = 100
b -= 7
print(b)
c = 44
c *=2
print(c)
d = 125
d /= 5
print(d)
e = 8
cube_e = e ** 3
print(cube_e)
f1 = 123
f2 = 345
print("f1 > f2")

current_hours = 14
current_minutes = 34
current_seconds = 42
daily_hours = 24
minutes_per_hour = 60
seconds_per_minutes = 60
total_seconds = current_hours * daily_hours * current_minutes * minutes_per_hour * current_seconds * seconds_per_minutes
remainin_seconds = total_seconds - daily_hours * minutes_per_hour * seconds_per_minutes
print("Remaining seconds from a day:", remainin_seconds)

Name = "Hello, Michael"
print(Name)

number = int(input ("Enter a number"))
if (number % 2) == 0:
    print(number," is an even Number")
else:
    print(number," is an odd Number")
number = int(input ("Enter a number"))
if number <= 0:
    print(number," Not enough")
elif number == 1:
    print(number," One")
elif number == 2:
    print(number," two")
else:
    print(number," A lot")
numberone = float(input ("enter a number"))
numbertwo = float(input ("enter a number"))
if numberone > numbertwo:
    print(numberone, "is bigger")
else:
    print(numbertwo, "is bigger")
n= int(input("enter a number:"))
for i in range(2, n+2):
    print("*" * 4)
