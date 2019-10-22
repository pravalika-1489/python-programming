'''to convert month name to no. of days'''
print("months: Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec")
month=input("enter the name of the month: ")
if month=="Feb":
    print("No. of days:28/29 days")
elif month in("Apr","Jun","Sep","Nov"):
    print("No.of days:30 days")
elif month in("Jan","Mar","May","Jul","Aug","Oct","Dec"):
    print("No.of days:31days")
else:
    print("invalid month")
