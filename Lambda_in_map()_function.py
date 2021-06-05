#Python
#lambda with map funtion
#declaring lambda function inside the map function argument
#Returns true or false
list1=["pink","purple","brown","pale yellow","white"]
map_object=map(lambda x: x[0]=="p",list1)   #map function
print(list(map_object))
