import cmath

# Function to solve the quadratic equation
def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = (b ** 2) - (4 * a * c)

    # Check the nature of the roots based on the discriminant
    if discriminant > 0:
        # Two distinct real roots
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        # One real root (repeated root)
        root = -b / (2 * a)
        return root
    else:
        # Complex roots
        real_part = -b / (2 * a)
        imaginary_part = cmath.sqrt(abs(discriminant)) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

# Get input coefficients from the user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Solve the quadratic equation
roots = solve_quadratic(a, b, c)

# Display the roots
if isinstance(roots, complex):
    print("Complex roots:")
    print("Root 1:", roots[0])
    print("Root 2:", roots[1])
else:
    print("Real roots:")
    print("Root 1:", roots[0])
    print("Root 2:", roots[1])
