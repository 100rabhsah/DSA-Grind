#Program to generate a random three-digit even number
import random
r = random.randint(100,999)
if(r%2==0):
    print(r)