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
print()

# Print a Christmas Tree
print("    *\n" "   ***\n" "  *****\n" " *******\n" "*********\n" "    |\n")

var = 0  # change to whatever
if var:
    print("true")
else:
    print("false")


print('"I\'m"' + "\n")
