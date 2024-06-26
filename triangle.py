def area_right_triangle(base, height):

  return 0.5 * base * height

def area_heron(side_a, side_b, side_c):

  if side_a <= 0 or side_b <= 0 or side_c <= 0:
    raise ValueError("Sides of a triangle must be positive numbers")
  
  # Semi-perimeter for Heron's formula
  semi_perimeter = (side_a + side_b + side_c) / 2
  
  # Area using Heron's formula
  area = math.sqrt(semi_perimeter * (semi_perimeter - side_a) * (semi_perimeter - side_b) * (semi_perimeter - side_c))
  return area
