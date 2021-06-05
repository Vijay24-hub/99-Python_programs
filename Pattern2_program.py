#Python
#Printing Pattern 
def Pattern2(number):
    for i in number:
        if i=="0":
            print("*******\n*     *\n*     *\n*     *\n*******\n")
        elif i=="1":
            print("   *   \n  **   \n   *   \n   *   \n*******\n")
        elif i=="2":
            print("*******\n      *\n*******\n*      \n*******\n")
        elif i=="3":
            print("*******\n      *\n*******\n      *\n*******\n")
        elif i=="4":
            print("*      \n*  *   \n*******\n   *   \n   *   \n")
        elif i=="5":
            print("*******\n*      \n*******\n      *\n*******\n")
        elif i=="6":
            print("*******\n*      \n*******\n*     *\n*******\n")
        elif i=="7":
            print("*******\n     * \n    *  \n   *   \n  *    \n")
        elif i=="8":
            print("*******\n*     *\n*******\n*     *\n*******\n")
        elif i=="9":
            print("*******\n*     *\n*******\n      *\n*******\n")
        else:
            print("Enter a valid value!!!")
number=input("Enter any number:")
Pattern2(number)    #Calling a function
