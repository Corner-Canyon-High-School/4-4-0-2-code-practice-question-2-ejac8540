red = int(input("Enter the red: "))
blue = int(input("Enter the blue: "))
green = int(input("Enter the green: "))
if red < 0 or red > 255:
    print("Red value is not correct.")
if blue < 0 or blue > 255:
    print("Blue value is not correct.")
if green < 0 or green > 255:
    print("Green value is not correct.")
if red >= 0 and red <= 255 and blue >= 0 and blue <= 255 and green >=0 and green <=255:
    print("No problems found!")