#Python
#StopIteration
#Use StopIteration to prevent to go on forever
class Tenmultiples:
    def __iter__(self):
        self.x=10
        return self
    def __next__(self): #if iteration is done raise an error
        if self.x<=100:
            a=self.x
            self.x+=10
            return a
        else:
            raise StopIteration
myobj=Tenmultiples()
myiter=iter(myobj)

for i in myiter: #continue forever till condition
    print(i)
        
