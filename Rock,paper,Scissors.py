h1="Rock"
h2="Paper"
h3="Scissor"
hand_1=input("enter the input you want to give? (Rock/Paper/Scissor) = ")
hand_2=input("enter the input you want to give? (Rock/Paper/Scissor) = ")
if hand_1==hand_2:
    print("Try again")
elif hand_1==h1 and hand_2==h2:  
    print("h2 wins")
elif hand_1==h1 and hand_2==h3:
    print("h1 wins")
elif hand_2==h2 and hand_1==h1:    
    print("h2 wins")
elif hand_2==h2 and hand_1==h3:    
    print("h3 wins")
elif hand_1==h3 and hand_2==h1:    
    print("h1 wins")
elif hand_1==h3 and hand_2==h2:    
    print("h3 wins")
else:    
    print("your input is not avaliable")