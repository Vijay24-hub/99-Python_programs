#Python
#OOPs concept
class Taxi:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Travel(Taxi):
    def fare(self):
        return super().fare() + self.capacity * 50
    
myobj= Travel("Cab", 100, 4)    #Instantiate of object
print(f"Total {myobj.name} fare is:", myobj.fare())

