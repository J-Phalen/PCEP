years = range(1583, 2027)
yearList = list(years)

for _, value in enumerate(yearList):
    year = value
    if year <= 1582:
        print("Not within the Gregorian calendar period.")
    elif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is a common year.")
