#Program for Fahrenheit to Celsius conversion

def ftoc(f):
    return (5/9)*(f-32)

f  = int(input("Enter Fahrenheit value:"))
print("The converted Celsius value is: ",ftoc(f))