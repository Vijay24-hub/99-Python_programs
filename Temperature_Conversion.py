#Python
#Temperature Conversion
#Celsius-->Fahreinheit
#Celsius-->Kelvin
def ConvertTemp(C):
    def ToFahrenheit():
        return (C*(9/5))+32
    print("Fahrenheit:",ToFahrenheit(),"F")
    def ToKelvin():
        return C+273.15
    print("Kelvin:",ToKelvin(),"K")
C=float(input("Enter the celsius value:"))
ConvertTemp(C)      #Calling a function
