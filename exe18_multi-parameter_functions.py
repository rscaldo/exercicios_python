""" Let's play with triangles now. We'll start with a function to check whether three sides of given lengths can build a triangle.

We know from school that the sum of two arbitrary sides has to be longer than the third side.

It won't be a hard challenge. The function will have three parameters ‒ one for each side.

It will return True if the sides can build a triangle, and False otherwise. In this case, is_a_triangle is a good name for such a function. """

def is_a_triangle(a, b, c):
  # return a + b > c and b + c > a and c + a > b
  if a + b <= c or a + c <= b or b + c <= a:
    return False
  else:
    return True

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))
print()


""" In the second step, we'll try to ensure that a certain triangle is a right-angle triangle.

We will need to make use of the Pythagorean theorem:

c2 = a2 + b2

How do we recognize which of the three sides is the hypotenuse?

The hypotenuse is the longest side. """

def is_a_triangle_2(a, b, c):
  return a + b > c and a + c > b and b + c > a

def is_a_right_triangle(a, b, c):
  if not is_a_triangle_2(a, b, c):
    return False
  if c > a and c > b:
    return c ** 2 == a ** 2 + b ** 2
  if a > b and a > c:
    return a ** 2 == b ** 2 + c ** 2
  if b > a and b > c:
    return b ** 2 == a ** 2 + c ** 2
  
print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))