side1 = float(input("Enter length of side1:\n"))
side2 = float(input("Enter length of side2:\n"))
side3 = float(input("Enter length of side3:\n"))
if (side1 == side2 == side3):
    print("Equilateral")
elif (side1 == side2 or side1 == side3 or side2 == side3):
    print("isosales")
else:
    print("Scalene")
