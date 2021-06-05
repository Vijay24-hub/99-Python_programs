#Python
#Json dumps
#Converting dictionary into string
import json
def json_dumps(dic):
    string=json.dumps(dic,indent=4)
    print(string)
    print(string[1:19]) #string slicing
dic={"Name":"zam",
     "age":21,
     "fees paid":True,
     "Attendance":85.3,
     "Arrears":None,
     "Cgpa":[
            {"Semester 1":7.43,
             "Semester 2":8.45,
             "Semester 3":7.02,
             "Semester 4":8.09}
         ]
     }
json_dumps(dic) #Calling a function
