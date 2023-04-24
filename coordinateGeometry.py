from math import sqrt
cord1 = input("Enter first coordinate seperated by ',' (syntax:(x, y): ")
cord1 = cord1.split(",")
cord1_x = int(cord1[0])
cord1_y = int(cord1[1])
print(cord1)


cord2 = input("Enter second coordinate seperated by ',' (syntax:(x, y): ")
cord2 = cord2.split(",")
cord2_x = int(cord2[0])
cord2_y = int(cord2[1])

x = int(input("1(Distance Formula) / 2(Mjdpoint Formula) : "))

if x == 1:
	y = sqrt(((cord2_x-cord1_x)**2)+((cord2_y-cord1_y)**2))
	print(f"The distance b/w ({cord1_x},{cord1_y}) & ({cord2_x},{cord2_y}) is {y}")
elif x == 2:
	res_x = (cord1_x + cord2_x) / 2
	res_y = (cord1_y + cord2_y) / 2
	print(f"The midpoint of ({cord1_x},{cord1_y}) & ({cord2_x},{cord2_y}) is ({res_x},{res_y})")
