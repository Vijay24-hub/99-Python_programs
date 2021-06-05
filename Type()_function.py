#Python
#Returning the type of a data types
def type_func():
    a="Hello"
    print(a,type(a))
    b=356
    print(b,type(b))
    c=23.5
    print(c,type(c))
    d=1j
    print(d,type(d))
    e=[1,"banana",True]
    print(e,type(e))
    f=("sea",34.5,False)
    print(f,type(f))
    g={3,6,7,8}
    print(g,type(g))
    h=range(9)
    print(h,type(h))
    i={"name":"apple","color":"red"}
    print(i,type(i))
    j=frozenset({"zeezee","meemee","keekee"})
    print(j,type(j))
    k=True
    print(k,type(k))
    l=b"Hehe"
    print(l,type(l))
    m=bytearray(7)
    print(m,type(m))
    n=memoryview(bytes(9))
    print(n,type(n))
type_func() #Calling a function
