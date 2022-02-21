class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return (self.width * self.height)

    # Just using the raw mathematical calculations because they are so simple and so much faster.
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        # Error case if the shape is too big
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ""
        # I would like to thank CS50 pset1 for my knowledge of this simple algorithm.
        for i in range(self.height):
            for j in range(self.width):
                picture += "*"
            picture += "\n"
        return picture

    def get_amount_inside(self, other):
        amount_inside = int(self.get_area() / other.get_area())
        return amount_inside

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

# All methods should be inherited just by including the parent class in the class declaration.


class Square(Rectangle):
    def __init__(self, side_length):
        self.width = self.height = side_length

    def set_side(self, new_side_length):
        self.set_width(new_side_length)
        self.set_height(new_side_length)

    def __str__(self):
        # Width and height are the same value, so it is irrelevant which one to return.
        return f"Square(side={self.width})"
