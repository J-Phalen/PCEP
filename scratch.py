###
# If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace in seconds per mile?
###

distance_km = 10
time_minutes = 42
time_seconds = 42
km_per_mile = 1.609

# Cast types here to make sure math works
total_time_seconds = (int(time_minutes) * 60) + int(time_seconds)
distance_miles = int(distance_km) / float(km_per_mile)
# dont need to cast here as the returns are typeset above
pace_seconds_per_mile = total_time_seconds / distance_miles

minutes = int(pace_seconds_per_mile // 60)  # Remove the decimal point with cast int
seconds = int(round(pace_seconds_per_mile % 60))  # Remove the decimal point with cast int

print(f"Average pace: {str(int(round(pace_seconds_per_mile))).zfill(3)} seconds per mile")
print(f"That is approximately {str(minutes).zfill(2)}:{str(seconds).zfill(2)} per mile")
print()  # blank space

# Print a Christmas Tree
print("This is a Christmas tree")
print("    *\n" "   ***\n" "  *****\n" " *******\n" "*********\n" "    |\n")
print()  # blank space

var = 0  # change to whatever
if var:
    print("true")
else:
    print("false")

print()  # blank space

print('"I\'m"' + "\n" + '"Learning"' + "\n" + '"Python"')
print()  # blank space


john = 3
mary = 5
adam = 6

print(f"John has {john} apples, Mary has {mary} apples, and Adam has {adam} apples.\n")
total_apples = john + mary + adam
print(f"Total Apples: {total_apples}\n")
print("John steals 2 of Adam's apples because he is a thief...\n")
adam -= 2
john += 2

# Reprint the same line with the new values
print(f"John has {john} apples, Mary has {mary} apples, and Adam has {adam} apples.")
print()


x = float(input("Enter a value for x: \n"))
y = 1 / (x + 1 / (x + 1 / (x + 1 / x)))
print("y = ", y)

# Get end time
hour = int(input("What is the hour of your start time?: \n"))
minutes = int(input("What is the minute of your start time?: \n"))
duration = int(input("How many minutes will the event last?: \n"))

# Convert the start time into total number of minutes
start_total_minutes = (hour * 60) + minutes

# Add in your duration minutes
end_total_minutes = start_total_minutes + duration

# Convert back to time formart
ending_hour = (end_total_minutes // 60) % 24
ending_minutes = end_total_minutes % 60

# Output the time
print(f"Endtime: {ending_hour}:{str(ending_minutes).zfill(2)}")
