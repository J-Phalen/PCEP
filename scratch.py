# If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace in seconds per mile?

distance_km = 10
time_minutes = 42
time_seconds = 42
km_per_mile = 1.609

total_time_seconds = (time_minutes * 60) + time_seconds
distance_miles = distance_km / km_per_mile
pace_seconds_per_mile = total_time_seconds / distance_miles

minutes = int(pace_seconds_per_mile // 60)
seconds = int(round(pace_seconds_per_mile % 60))

print(f"Average pace: {str(int(round(pace_seconds_per_mile))).zfill(3)} seconds per mile")
print(f"That is approximately {str(minutes).zfill(2)}:{str(seconds).zfill(2)} per mile")


print("    *\n" "   ***\n" "  *****\n" " *******\n" "*********\n" "    |\n")
