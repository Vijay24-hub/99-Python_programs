#Python
#OOPs concept
class PrintString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input("Enter the string:")

    def print_String(self):
        print(self.str1.upper())

myobj= PrintString()    #Instantiate of object
myobj.get_String()
myobj.print_String()
