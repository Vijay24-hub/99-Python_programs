#Python
#Converting decimal into other number systems
def ConvertDecimal(dec_num):
    print("The decimal value of", dec_num, "is:")
    print(bin(dec_num), "in binary.")
    print(oct(dec_num), "in octal.")
    print(hex(dec_num), "in hexadecimal.")
dec_num = int(input("Give a decimal number:"))
ConvertDecimal(dec_num) #Calling a function
