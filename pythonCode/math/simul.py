# Function to solve a system of simultaneous equations
def solve_simultaneous_equations(a1, b1, c1, a2, b2, c2):
    # Solve for x using the substitution method
    x = (b2 * c1 - b1 * c2) / (a1 * b2 - a2 * b1)

    # Substitute x into either equation to solve for y
    y = (c1 - a1 * x) / b1

    return x, y


# Get input coefficients from the user
a1 = float(input("Enter coefficient a1: "))
b1 = float(input("Enter coefficient b1: "))
c1 = float(input("Enter coefficient c1: "))

a2 = float(input("Enter coefficient a2: "))
b2 = float(input("Enter coefficient b2: "))
c2 = float(input("Enter coefficient c2: "))

# Solve the system of simultaneous equations
solution = solve_simultaneous_equations(a1, b1, c1, a2, b2, c2)

# Display the solution
print("Solution:")
print("x =", solution[0])
print("y =", solution[1])
