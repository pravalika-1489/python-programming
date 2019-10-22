'''to find median of 3 values'''
x=float(input("enter 1 no: "))
y=float(input("enter 2 no: "))
z=float(input("enter 3 no: "))
if x>y:
    if x<z:
        median=x
    elif y>z:
        median=y
    else:
        median=z
else:
    if x>x:
        median=x
    elif y<z:
        median=y
    else:
        median=z
print("the median is ",median)
        
