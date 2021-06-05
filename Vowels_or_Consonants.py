#Python
#Find the characters of the string
#Is Vowels(a,e,i,o,u) or Consonants
def my_func(string):
    for i in string:
        if "a"==i or "e"==i or "i"==i or "o"==i or "u"==i:
            print("vowel:",i)
        else:
            print("consonant:",i)

string=input("Enter the string:")
my_func(string)     #Calling a function
