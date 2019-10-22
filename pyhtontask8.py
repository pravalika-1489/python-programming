'''python func to multiply all the no.s in a list'''
def multiply(nos):
    total=1
    for x in nos:
        total*= x
    return total
print(multiply((6,7,8,4,3)))
