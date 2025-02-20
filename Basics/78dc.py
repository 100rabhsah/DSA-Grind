#Program to convert time from 12 hour to 24 hour format

time_12 = input("Enter time in 12-hour format (hh:mm:ss AM/PM): ")

time_part, period = time_12.split()
hours, minutes, seconds = map(int, time_part.split(":"))

if period.upper() == "AM":
    if hours == 12:  # 12 AM is 00 hours in 24-hour format
        hours = 0
elif period.upper() == "PM":
    if hours != 12:  # For PM hours (except 12 PM), add 12
        hours += 12

print(f"Time in 24-hour format: {hours:02}:{minutes:02}:{seconds:02}")
