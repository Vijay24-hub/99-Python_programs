#Python
#Nested dictionary
def myfunc(dict1,dict2,dict3,dict4):
    Players={
            "player1":dict1,
            "player2":dict2,
            "player3":dict3,
            "player4":dict4}
    print(Players)
dict1={"Name":"Dhoni",
       "Role":["Captain","Batsman","Wicketkeeper"],
       "Team":"CSK"}
dict2={"Name":"Kholi",
       "Role":["Captain","Batsman"],
       "Team":"RCB"}
dict3={"Name":"Raina",
       "Role":"Batsman",
       "Team":"CSK"}
dict4={"Name":"Jadeja",
      "Role":["Batsman","Bowler"],
      "Team":"CSK"}
myfunc(dict1,dict2,dict3,dict4) #Calling a function
