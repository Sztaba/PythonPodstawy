#1
import math

#2
#1 rad = 1° * π / 180°
#1° = 1 rad * 180° / π

#3
degree=360
print(degree*math.pi/180)

#4
degree=45
print(degree*math.pi/180)

#5
print(math.radians(360),math.radians(45))

#6
small_pizza_r=22
big_pizza_r=27
family_pizza_r=38
small_pizza_price=11.50
big_pizza_price=15.60
family_pizza_price=22.00

#7
print(small_pizza_r**2*math.pi)
print(big_pizza_r**2*math.pi)
print(family_pizza_r**2*math.pi)

#8
print(small_pizza_price/small_pizza_r**2*math.pi)
print(big_pizza_price/big_pizza_r**2*math.pi)
print(family_pizza_price/family_pizza_r**2*math.pi)

#9 WYSWIETLENIE WSZYSTKICH FUNKCJI - Strona z opisami: https://docs.python.org/2/library/math.html
print(dir(math))