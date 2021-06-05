#Python
#Reversing the words of a given string
def rev_sentence(sen):
    words=sen.split(" ")
    sentence=" ".join(reversed(words))  
    return sentence
sen=input("Enter the sentence to be reversed:")
print("The reversed words in a given string:{0}".format(rev_sentence(sen))) #Calling a function
