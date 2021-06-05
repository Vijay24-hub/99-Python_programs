#Python
#check if the given number
#is prime number or anything else
def check_prime_number(number):
    if number<0:
        return "Negative integer"
    elif number==0:
        return "Neither prime nor composite"
    elif number==1:
        return "Not a prime number"
    else:
        for i in range(2,number):
            if number%i==0:
                return "Not a prime number"
        else:
            return "Is a Prime number"
number=int(input("Enter the number to check that the number is prime number or not:"))
print(check_prime_number(number))   #Calling a function
