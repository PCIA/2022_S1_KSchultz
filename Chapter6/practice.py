x = True
while x == True:
    y = input("Give a whole number")
    if y >= 10 and y <= 20:
        print(int(y**2))
    elif y < 10:
        print("Too low")
    elif y > 20:
        print("Too high")
    x == False
    
