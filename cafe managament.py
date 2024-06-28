menu = {
    'pizza':100,
    'pasta':60,
    'coffe':60,
    'salad':80,
    'maggie':70
}
print("Welcome to NISA")
print("pizza: Rs100\npasta: Rs60\ncoffe: Rs60\nsalad: Rs80\nmaggie: Rs70")
order_total=0
item_1 = input("enter the item you want to order=")
if item_1 in menu:
    order_total=order_total+menu[item_1]
    print(f"your {item_1} has been added to order")
else:   
    print(f"{item_1} is not avaliable")
another_order=input("do you want to order anything else? yes/no ")
if another_order=="yes":
    item_2=input("enter the item you want to order")
    if item_2 in menu:
        order_total=order_total+menu[item_2]
        print(f"your {item_2} has been added to order")
    else:        
        print(f"your {item_2} is not avaliable")
else:        
    print("Thank you sir")
print("your Total bill =",order_total)




