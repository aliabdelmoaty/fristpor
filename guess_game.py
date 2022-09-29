from ast import Try
from pickle import FALSE, TRUE
while TRUE :

    frist_player = input("Enter your secred word: ")
    two_player =""
    fristtry = 1
    three_trY = 3
    guess_out = False
    while frist_player != two_player and not guess_out :
        two_player = input("Enter your word: ")
        if frist_player == two_player:
            print("you win")
    
        if fristtry < three_trY :
        
            fristtry +=1
    
        else:
            guess_out = True 
            print("you lose")
    again= str.lower(input("play again?\nYes or No? ")) 
    if again == "no":
        print("i'm sorry for you leave")
        break           
    
