'''to check a triangle is equ,iso or scalen'''
print("enter length of triangle sides: ")
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
if a==b==c:
    print("equilateral triangle")
elif a==b or b==c or c==a:
    print("isosceles triangle")
else:
    print("scalen trianle")
