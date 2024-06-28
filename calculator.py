a=int(input("enter the value = "))
b=int(input("enter the value = "))
operation_1="+"
operation_2="-"
operation_3="*"
operation_4="/"
c=a+b
d=a-b
e=a*b
f=a/b
operation=input("enter the operation you want to perform")
if operation==operation_1:
    print(c)
elif operation==operation_2:    
    print(d)
elif operation==operation_3:    
    print(e)
elif operation==operation_4:    
    print(f)
else:    
    print("operation is not found")
