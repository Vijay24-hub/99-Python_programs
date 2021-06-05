#Python
#lambda funtion with filter function
#Returns object which satisfies the condition with lambda
list1=["bike","car","scooter","truck","van"]
filter_object=filter(lambda s:s[1]=="a",list1)  #filter() function
print(list(filter_object))
