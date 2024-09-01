#  - Calculate your age based on the current year and your birth 
currentyear = int(input ("currentyear ="))
birthyear = int(input("birthyear ="))
age = currentyear - birthyear
print ("age=", age)

# - Calculate your age based on the current year and your birth 
def current_age (currentyear , birthyear):
    return currentyear - birthyear
print ("current_age=", current_age(2024 , 2013))






# - Write a program that calculates the area of a rectangle using length and width variables.
lenght = int(input("lenght = "))
widht = int(input("widht ="))
area = lenght * widht
print ("area=", area)

def areaofrectangule (lenght , widht):
    return lenght * widht
print ("areaofrectangule=", areaofrectangule(10 , 5))

#  - Write a program that calculates the area of a circle.
import math
radius =int(input("radius = "))
areaofcircle = math . pi *radius ** 2
print ("areaofcircle=", areaofcircle)


def areaofcircle (radius):
    return math . pi * radius ** 2
print ("areaofcircle=", areaofcircle(100))

# - Write a program that calculates the area of a cube.
side = int(input("side ="))
areaofside = 6 * side **2
print ("areaofside=", areaofside) 

def areaofcube (side):
    return 6 * side ** 2 
print ("areaofcube=", areaofcube(100))

# - Create a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable.




f = int(input("f ="))
c : int = 5/9 * (f - 32)
print ("c=", c)

c = int(input("c =")) 
f : int = (c * 9/5) + 32
print ("f=", f)

def c2f (c):
    return 5/6 *(c - 32)
print ("c2f="(37.77778))

def f2c (f):
    return (f * 9/5) + 32
print ("f2c =", f2c(100))

# - Write a program that calculates the percentage.
totalmark = int(input("totalmark ="))
markobtained = int(input("markobtained ="))
persontageofmark : int = markobtained / totalmark
print ("Cofmark=", persontageofmark)

def persontage (totalmark , markobtained):
    return markobtained / totalmark * 100
print ("persontage=", persontage(100 , 90))

# - Convert a given number of seconds into minutes and seconds using variables.
sec = int(input("sec = "))
secinmin : int = 60
min = sec / secinmin 
print ("min =", min)

def sec (sec):
    return sec / 60
print ("mn=", min(3600))

# - Write a program that calculates the BMI using height (in meters) and weight (in kilograms) variables.
weight = float(input("weight = "))
height = float(input("height = "))

bmi = weight / height**2
print ("divide=", bmi)

def BMI (weight,height):
    return weight / height **2
print ("divide=", BMI(60,1.5))

# - Write a program that calculates the volume of a cylinder using the formula .
import math
radius = int(input("radius = "))
height = int(input("height = "))
volumofclyinder : int = math.pi *radius ** 2 * height
print ("volumofclyinder=", volumofclyinder)

def radius (radius , height):
    return math.pi * radius**2*height
print ("volumofclyinder=", radius(10 , 5))