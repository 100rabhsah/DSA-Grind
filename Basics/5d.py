#Write a program to print 1 to 100 without using any numerical value

for i in range(ord('a'), ord('a')+100):  # 'a' -> 97, 'd' -> 100
    print(i - ord('a') + 1)