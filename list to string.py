 #How to convert a list into a string?
##l=["shilpa","sonal","jadhao","class"]
##s=" ".join(l)
##print(s)


##How to convert a list into a tuple?
##l=["shilpa","sonal","jadhao","class"]
##print(tuple(l))


##How to convert a list into a set?
##l=["shilpa","sonal","jadhao","class"]
##print(set(l))



##How to count the occurrences of a particular element in the list?
##def sume(l,n):
##    c=0
##    for i in l:
##        if i==n:
##            c=c+1
##    print(c)
##
##
##sume(l=[1,2,3,4,12,2,3,2],n=int(input("please enter the value:-")))


##import numpy
##numpy.array([])
##A=numpy.array([1,2,3])
##print(A)
##Jump to Array Using arange()
##and shape() - Let's start with a one-dimensional NumPy array.
##import numpy as np.
##A = np. array([2, 4, 6, 8, 10])
##print("A[0] =", A[0]) # First element. print("A[2] =", A[2])
### Third element. print("A[-1] =", A[-1]) # Last element.



##min and max from list
##l=[2, 4, 6, 8, 10]
##l.sort()
##print("the secon min number present in list is",l[1])
##min=8
##for i in l:
##    if i<min:
##        min=i
##print(min)



##max=4
##for i in l:
##    if i>max:
##        max=i
##
##print(max)
"""sum of all list"""

##l=[2, 4, 6, 8, 10]
##sum=0
##for i in l:
##    sum=sum+i
##
##print(sum)


'''To display the sum of first n numbers'''
##n=int(input("please enter the number which you want to add from the number:-"))
##sum=0
##i=1
##while i<=n:
##    sum=sum+i
##    i=i+1
##print(sum)


'''right angle tringlle
1) *
2) * *
3) * * *
4) * * * *
5) * * * * *
6) * * * * * *
7) * * * * * * *

'''

##for i in range(1,8):
##    print("*"*i)



''' inpuut
1)       *
2)      * *
3)     * * *
4)    * * * *
5)   * * * * *
6)  * * * * * *
7) * * * * * * *  
'''

##for i in range(1,8):
##    print(" "*(8-i),end=" ")
##    print("* "*i)



s="shilpajadhao"
print(s.find("a"))
print(s.index("o"))

print(s.count("a",0,4))











































