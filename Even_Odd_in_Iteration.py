#Python
#Find Even and odd Using Iteration
class EvenOddIteration:
    def __init__(self,max):
        self.a=1
        self.max=max
    def __iter__(self):
        return self
    def __next__(self):
        while self.a<=self.max:
            if self.a%2==0:
                print("Even:",self.a)
            else:
                print("Odd:",self.a)
            self.a+=1
        else:
            raise StopIteration
myobj=EvenOddIteration(20) #Object
myiter=iter(myobj)

for i in myiter:
    print(i)
