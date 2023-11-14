# def my_decorator(func):
#     def wrapper():
#         print('before decorator')
#         func()
#         print('after decorator')
#     return wrapper
#
#
# @my_decorator
# def hello():
#     print('hello')
#
# hello()

# class Vector:
#
#     '''fdgdfgdd'''
#     MIN_COORD = 0
#     MAX_COORD = 100
#
#     def __init__(self, x, y):
#         self.x = self.y = 0
#         if self.validate(x):
#             self.x = x
#
#         if self.validate(y):
#             self.y = y
#
#         print(Vector.norm2(self.x, self.y))
#         print(self.norm2(self.x, self.y))
#
#     def get_coords(self):
#         return self.x, self.y
#
#     @staticmethod
#     def norm2(x, y):
#         return x ** 2 + y ** 2
#
#     @classmethod
#     def validate(cls, arg):
#         return cls.MIN_COORD < arg < cls.MAX_COORD
#
#
# v = Vector(1,5)
# print(v.norm2(1, 8))
# print(v.__dict__)
# print(Vector.norm2(1,8))


# from math import pi
#
# class Cylinder:
#
#     @staticmethod
#     def make_area(d, h):
#         circle = pi * d ** 2 / 4
#         side = pi * d * h
#         return circle * 2 + side
#
#     def __init__(self, diam, high):
#         self.diam = diam
#         self.high = high
#         self.area = self.make_area(self.diam, self.high)
#
#     def __str__(self):
#          return f'diam = {self.diam}, high = {self.high}, area = {self.area}'
#
# c = Cylinder(2, 4)
# print(c)
# print(c.__dict__)

#
# class MyClass:
#     TOTAL_COUNTS = 0
#
#     def __init__(self):
#         MyClass.TOTAL_COUNTS = MyClass.TOTAL_COUNTS + 1
#
#     @classmethod
#     def total_counts(cls):
#         print('total counts =', cls.TOTAL_COUNTS)
#
#
# class ChildClass(MyClass):
#     TOTAL_COUNTS = 0
#
#     def __init__(self):
#         ChildClass.TOTAL_COUNTS += 1
#
# m = MyClass()
# m1 = MyClass()
# MyClass.total_counts()
# cc = ChildClass()
# cc.total_counts()

# class Point:
#     MIN_COORD = 0
#     MAX_COORD = 100
#     z = 123123
#
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.y = y
#
#     def set_coord(self, x, y):
#         if self.MIN_COORD < x < self.MAX_COORD:
#             self.x = x
#         if self.MIN_COORD < y < self.MAX_COORD:
#             self.y = y
#
#     @classmethod
#     def set_bound(self, left):
#         self.MIN_COORD = left
#
#     def __getattribute__(self, item):
#         if item == '_POint__x':
#             raise ValueError
#         return object.__getattribute__(self, item)
#
#     def __str__(self):
#         return f'x = {self.x} , y = {self.y}'
#
#     def __setattr__(self, key, value):
#         if key == 'z':
#             raise ValueError
#         else:
#             self.__dict__[key] = value
#
#     def __getattr__(self, item):
#         print('getattr ' + item)
#
#     def __delattr__(self, item):
#         object.__delattr__(self, item)
#
#     def __del__(self):
#         print('no object')
#
# p = Point(1, 6)
# p.j = 15
# Point.__setattr__(p, 'k', 154)
# print(p.__dict__)
# print(p.l)

class Snow:
    def __init__(self, num):
        self.num = num

    def make_snow(self, el):
        for i in range(self.num // el):
            print('*' * el)
        print('*' * (self.num % el))

    def __add__(self, other):
        if not isinstance(other, (int, Snow)):
            raise TypeError

        # if isinstance(other, int):
        #     res = other
        # else:
        #     res = other.num
        res = other if isinstance(other, int) else other.num
        return Snow(self.num + res)

    def __sub__(self, other):
        if not isinstance(other, (int, Snow)):
            raise TypeError
        res = other if isinstance(other, int) else other.num
        return Snow(self.num - res)

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError
        return Snow(self.num * other)

    def __floordiv__(self, other):
        if not isinstance(other, int):
            raise TypeError
        return Snow(self.num // other)

    def __truediv__(self, other):
        if not isinstance(other, int):
            raise TypeError
        return Snow(self.num // other)


s = Snow(1000)
s1 = Snow(10)
s2 = s / 10
s2.make_snow(100)