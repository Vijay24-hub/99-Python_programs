#Python
#loads method in Json
#Converts string into the dictionary
import json
def json_loads(string):
    dic=json.loads(string)
    print(dic["Brand"])
    dic["color"]="black"    #adding new key and value
    print(dic)
string='{"vehicle":"Bike","Brand":"yamaha","Model":"Fz","Year":"2021"}'
json_loads(string)  #Calling a function
