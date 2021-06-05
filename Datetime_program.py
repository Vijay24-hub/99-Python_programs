#Python
#dateandtime funtion
import datetime as D
x=D.datetime.now()
print("***CURRENT DATE TIME***")
print("Date and time:",x)   #Current date and time
print("Day:",x.strftime("%d"))  #current day
print("Month:",x.strftime("%m"))    #current month 
print("Year",x.strftime("%Y"))  #current Year
print("Hours:",x.strftime("%I"))    #current hours timing
print("Minutes:",x.strftime("%M"))  #current minutes timing
print("Seconds:",x.strftime("%S"))  #current seconds timing
print("AM/PM:",x.strftime("%p"))    #am or pm
print("Day name:",x.strftime("%A")) #Day in name
print("Month name:",x.strftime("%B"))   #month in name
