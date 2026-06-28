def hello():
    print("Hello World")

print(hello())

def math():
    return 1,2,[2,3]

print(math())


a=10

def add(a,b):
    return a+b

print(add(10,20))


def userinfo(fname,lname):
    return f'My name is {fname} {lname}'

print(userinfo('Bidur','Khanal'))
print(userinfo('Khanal','Bidur'))

#key Word Argument

print(userinfo(lname='khanal',fname='Bidur'))
