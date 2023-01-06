# class that represents a Rectangle
class Rectangle:
    # initialized with width and height inputs
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # string representation
    def __str__(self):
        return 'Rectangle(width={width}, height={height})'.format(width=self.width, height=self.height)

    # method that changes the width
    def set_width(self, width):
        self.width = width

    # method that changes the height
    def set_height(self, height):
        self.height = height

    # method that returns the area of the rectangle
    def get_area(self):
        return self.width * self.height

    # method that returns the perimeter of the rectangle
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    # method that returns the length of a diagonal
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    # method that returns lines of asterisks which represent the rectangle
    def get_picture(self):
        if self.width > 50 or self.width > 50:
            return 'Too big for picture.'
        else:
            return (('*' * self.width) + '\n') * self.height

    # method that calculates how many of the other rectangles can fit in the self rectangle
    def get_amount_inside(self, other):
        return (self.width // other.width) * (self.height // other.height)


# class Square that is a sub class of Rectangle
class Square(Rectangle):
    def __init__(self, side, width=None, height=None):
        self.side = side
        if width is None:
            self.width = side
        if height is None:
            self.height = side

    def __str__(self):
        return 'Square(side={})'.format(self.side)

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_width(self, width):
        self.side = width
        self.width = width
        self.height = width

    def set_height(self, height):
        self.side = height
        self.width = height
        self.height = height
