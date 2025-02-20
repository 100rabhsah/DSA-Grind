#Convert time from 24 hour clock to 12 hour clock format

time_24 = input("Enter time in 24-hour format (hh:mm:ss AM/PM): ")

time_part, period = time_24.split()
hours, minutes, seconds = map(int, time_part.split(":"))

if period.upper() == "AM":
    if hours == 12: 
        hours = 0
elif period.upper() == "PM":
    if hours != 12:  
        hours -= 12

print(f"Time in 12-hour format: {hours:02}:{minutes:02}:{seconds:02}")
