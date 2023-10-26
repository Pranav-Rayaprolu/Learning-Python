x=int(input("enter your first number"))
y=int(input("enter your second number"))
z=input("enter your operator")
if(z=="+"):
    print("the sum is ",x+y)
if(z=="-"):
    print(x-y)
if(z=="*"):
    print(x*y)
if(z=="/"):
    print(x/y)
if(z=="**"):
    print(x**y)    
else:
    print("invalid operator")
    