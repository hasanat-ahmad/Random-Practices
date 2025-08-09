side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

if side1 == side2 == side3:
    triangle_type = "Equilateral Triangle"
elif side1 == side2 or side2 == side3 or side1 == side3:
    triangle_type = "Isosceles Triangle"
else:
    triangle_type = "Scalene Triangle"

print(f"The triangle is a {triangle_type}.")
