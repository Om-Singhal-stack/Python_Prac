from datetime import date

date = date.today()

current_year = date.year
name = input("enter your name")
age = int(input("enter your age"))
after_cal = (current_year-age)+100
print(name,"you will be turn to 100 in ",after_cal)