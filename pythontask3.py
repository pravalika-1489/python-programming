'''python function that takes a list of words & returns the length of the longest one'''
l=[]
n=int(input("enter no.of elements in list: "))
for x in range(0,n):
    element=input("enter element "+str(x+1)+":")
    l.append(element)
    l.append(element)
max1=len(l[0])
temp=l[0]
for i in l:
    if(len(i)>max1):
        max1=len(i)
        temp=i
print("longest length is: ")
print(temp)
