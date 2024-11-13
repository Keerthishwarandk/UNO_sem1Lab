class overloading:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Overloading the + operator
    def __add__(self, other):
        return overloading(self.x + other.x, self.y + other.y)

    # Overloading the - operator
    def __sub__(self, other):
        return overloading(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Creating two Point objects

a=int(input("Enter set 1  value 1  "))
b=int(input("Enter set 1  value 2  "))
c=int(input("Enter set 2  value 1  "))
d=int(input("Enter set 2  value 2  "))
p1 = overloading(a, b)
p2 = overloading(c, d)

# Using the overloaded + operator
p3 = p1 + p2
print(f"The Addition Value {p3}")  # Output: (4, 6)

# Using the overloaded - operator
p4 = p1 - p2
print(f"The subtracted value {p4}")  # Output: (-2, -2)
