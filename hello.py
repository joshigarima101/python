print ("hello world")
#hi this is a comment
#print ("hello")
"""
hi this is a comment written
in more
than one
line
"""
x=5 #this is type int
y="john" #this is type string
# x and y are variables. variables are containers for storing data values.
print (x)
print (y)
#if you want to specify the data type of a variable
x=str(3)
y=int(4)
z=float(3)
print (x,y,z)

x=5
y="john"
print (type(x)) #this prints the data type

# variable must start with a letter or an underscore and cannot start with a number.
#variable is case sensitive so A and a are different.

x,y,z="Orange", "Banana", "Cherry"
print (x)
print(x,y,z)
x = y = z = "red"
print(z)

colours=["red", "blue","yellow","green"]
l,m,n,o= colours
print(l,m,n,o)

x="python is awesome"
print(x)

x="python"
y="is"
z="awesome"
print(x,y,z) #space
print(x+y+z) #not spaced

#you can only use + on same data type for eg 5+10 or python+hello not 5+python

'''a global variable can be used anywhere but a local variable can be used inside the function only'''

x= "hi"

def myfunc():
    x="herro"
    print(x + " hibachi benihana teriyaki")
myfunc()

print(x,"how are u")
