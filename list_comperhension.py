a=[1,2,3,4,5]

#before list comperhensionn
result=[]
for i in a:
    result.append(i*i)

print(result)

#After List Comperhension

result=[i**2 for i in a]

print(result)

square=lambda *args:[i**2 for i in args]

print(square)