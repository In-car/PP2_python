#we can import datetime to work with dates 
#date is not a data type 
import datetime 

x = datetime.datetime.now()
print(x)


#datetime has a lot of methods 
#returns year
print(x.year)
#returns name of the weekday 
print(x.strftime("%A"))


#to create a date , we use datetime() class of the datetime module 
y = datetime.datetime(2007, 2, 25)
print(y)


#the datetime() can also take parameters for time and timezone 
#(hour, minute, second, microsecond, tzone)


#strftime() takes one parameter,format, to specify
# the format of the returning string 
import datetime

x = datetime.datetime(2020, 1, 24)

print(x.strftime("%B"))


#we have a lot of format codes 
#like %a is weekday,short version something like "Wed"
# but the %A is the full version of it : "Wednesday" 
