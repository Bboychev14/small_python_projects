# Fibbonaci

# def fibb(num):
#     if num < 1:
#         raise ValueError("Your input should be > 0")
#     a, b = 0, 1
#     for i in range(num - 1):
#         yield a
#         a, b = b, a + b
#     yield a
#
# try:
#     for i in fibb(0):
#         print(i, end=', ')
# except ValueError as e:
#     print(f"Error: {e}")

# ----------------------------------------------------------------------------------------------------

# Factorial / + recursion

# def factorial(num):
#     if num == 0:
#         return 1
#     return num * factorial(num - 1)
#
# def factorial(num):
#     result = 1
#     for i in range(2, num + 1):
#         result *= i
#     return result
#
# print(factorial(5))

# from abc import ABC, abstractmethod
# class Shape(ABC):
#     def __init__(self, side):
#         self._side = side
#
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#
# class Square(Shape):
#     def __init__(self, side):
#         super().__init__(side)
#
#     def area(self):
#         return self._side ** 2
#
#     def perimeter(self):
#         return self._side * 4
#
#
# class Triangle(Shape):
#     def __init__(self, side, h):
#         super().__init__(side)
#         self.__h = h
#
#     def area(self):
#         return self._side / 2 * self.__h
#
#     def perimeter(self):
#         return "fake P"
#
#
# class EquilateralTriangle(Triangle):
#     def __init__(self, side, h):
#         super().__init__(side, h)
#
#     def perimeter(self):
#         return self._side * 3
#
#
# square = Square(5)
# print(square.area())
# print(square.perimeter())
# triangle = Triangle(6, 8)
# print(triangle.area())
# print(triangle.perimeter())
# equilateral_triangle = EquilateralTriangle(4, 3)
# print(equilateral_triangle.perimeter())
# print(equilateral_triangle.area())



# Christmas Tree

# def printChristmasTree(h):
#     for i in range(1, h + 1):
#         spaces = ' ' * (h - i)
#         stars = '*' * (i * 2 - 1)
#         print(spaces + stars)
# printChristmasTree(6)

