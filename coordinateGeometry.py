cord1 = input("Enter first coordinate seperated by ',' (syntax:(x, y): ")
cord1 = cord1.split(",")
cord1_x = int(cord1[0])
cord1_y = int(cord1[1])
print(cord1)


cord2 = input("Enter second coordinate seperated by ',' (syntax:(x, y): ")
cord2 = cord2.split(",")
cord2_x = int(cord2[0])
cord2_y = int(cord2[1])

res_x = (cord1_x + cord2_x) / 2
res_y = (cord1_y + cord2_y) / 2

print(f"{res_x},{res_y}")
