# main.py

from shapes import Rectangle, Circle

def main():
    # Create a rectangle and calculate its area and perimeter
    rect = Rectangle(width=10, height=5)
    print(f"Rectangle Area: {rect.area()}")
    print(f"Rectangle Perimeter: {rect.perimeter()}")

    # Create a circle and calculate its area and circumference
    circle = Circle(radius=7)
    print(f"Circle Area: {circle.area()}")
    print(f"Circle Circumference: {circle.circumference()}")

if __name__ == "__main__":
    main()
