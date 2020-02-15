'''a=[1,"m",56.56778,True]
print(a)
for i in a:
    print(i,"type :",type(i))
'''
import numpy
a=[1,2,3,4,5,6]
b=numpy.array(a)
print(b[0:2])
print(b[2:4])
print(b[4:6])

