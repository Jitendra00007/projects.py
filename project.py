import random
operation=["Rock","Scissor","Paper"]
"""
Pock vs Paper :- paper wins
Rock vs Scisssor:- rock win
Paper vs Scissor:- scissor win
"""
while True:
    computer_count=0
    user_count=0
    user_choice=int(input("""
    same start
    1 Yes
    2 No(exit)"""))
    if user_choice==1:
        for a in range(1,6):
            user_input=int(input("""
    1 Rock
    2 Scissor 
    3 Paper       """))
            if user_input==1:
                uchoice="Rock"
            elif user_input==2:
                uchoice="Scissor"
            elif user_input==3:
                uchoice="Paper"
            else:
                print("invalid input")

            com_choice=random.choice(operation)
            if uchoice==com_choice:
                print("computer choice:-",com_choice)
                print("you choice:-",uchoice)
                print("game draw")
                user_count=user_count+1
                computer_count=computer_count+1
            elif(uchoice=="Rock" and com_choice=="Scissor") or (uchoice=="Paper" and com_choice=="Rock") or (uchoice=="Scissor" and com_choice=="Paper"):
                 print("computer choice:-",com_choice)
                 print("you choice:-",uchoice)
                 print("you win")
                 user_count=user_count+1
            else:
                print("computer choice:-",com_choice)
                print("you choice:-",uchoice)
                print("com win")
                computer_count=computer_count+1

            if user_count==computer_count:
             print("FINALLY GAME DRAW....")
             print("YOU SCORE:-",user_count)
             print("COMPUTER SCORE:-",computer_count)
            elif user_count>computer_count:
             print("FINALLY YOU WIN...")
             print("YOU SCORE:-", user_count)
             print("COMPUTER SCORE:-", computer_count)
            else:
             print(" FINALLY COMPUTER WIN")
             print("YOU SCORE:-", user_count)
             print("COMPUTER SCORE:-", computer_count)







    else:
        break