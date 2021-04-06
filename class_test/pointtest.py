from class_test.ColorPoint import ColorPoint
from class_test.Point import Point



p1 = Point(10,20)
p1.draw()

p2 = ColorPoint('red', 30, 50)
p2.draw()
print(type(p2))
print(p2)

i = 10
print(type(i))
print(i)

print(Point.count_of_instance)