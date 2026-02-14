try:
    year = int(input("Enter a year: "))
except ValueError:
    print("Invalid input. Please enter a numeric value for the year.")
    exit(1)

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is a common year.")
