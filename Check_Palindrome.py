#Python
#checking the string is palindrome or not
def check_Palindrome(strr):
    reverse=strr[::-1]  #Reversing the string
    print("after reverse:",reverse)
    if strr==reverse:   #checking for palindrome
        print("Palindrome")
    else:
        print("Not a Palindrome")
strr=input("Enter the string to check that the string is Palindrome or not:")
print("before reverse",strr)
check_Palindrome(strr)  #calling a function
