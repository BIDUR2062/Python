class Test():
    a=10
    b=11

obj=Test()
obj.a="changed"
obj.c="new value"
print(obj.a)

print(obj.c)

obj1=Test()
print(obj1.a)
# print(obj1.c)

#print(obj == obj1)

class Test2():
    a=10
    b=11

    def add(self,d):
        self.c=100
        self.d=d
        return d+self.b
    
    def sub(self):
        print(self.d)
        return self.a-self.b
    
    def result(self):
        return self.add(10)+self.sub()

obj=Test2()
# print(obj.add(10))
# print(obj.sub())
# obj.a=21
# print(obj.c)
# print(obj.add())
print(obj.result())

class Test3():
    def __init__(self,a,b):
        print("testing")
        self.a=a
        self.b=b
        print(self.a)
        print(self.b)
        return
    
obj=Test3(1,2)
        
class Test4():
    a=10
    message="testing-message"

    def __str__(self):
        return self.message

obj=Test4()
print(obj)


class Test5():
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(a,b)
    
    def add(self):
        return self.a+self.b
    
obj=Test5(50,1)
print(obj.add())