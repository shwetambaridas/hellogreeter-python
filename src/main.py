from datetime import date

#Input asking name
name = input("What is your name? ")

#ask for the birth year and calculate age
birth_year = int(input("What year were you born? "))
current_year = date.today().year
calculated_age = current_year - birth_year

#print greeting
print(f"Hello, "+ name + "")
print(f" You are {calculated_age} years old!")
print(f" You will be {calculated_age + 1} years old next year!")

