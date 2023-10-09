import random
# Printing instructions
print("Winning rules of the game ROCK PAPER SCISSORS are :\n" + "Rock vs Paper -> Paper wins \n" + "Rock vs Scissors -> Rock wins \n" + "Paper vs Scissors -> Scissor wins \n")
while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    # Getting user input
    choice=int(input("Enter your choice :"))
    # looping the valid user input
    while(choice < 1 or choice > 3):
        choice = int(input("Please enter a valid choice: "))
    
    # Initialinzing user's choice
    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissors"
    print('User choice is \n',choice_name)
    
    print('Now its Computers Turn....')
    # Setting Computer's choice
    comp_choice = random.randint(1,3)
    
    # Initialinzing computer's choice
    if comp_choice == 1:
        comp_choice_name = "rocK"
    elif comp_choice == 2:
        comp_choice_name = "papeR"
    else:
        comp_choice_name = "scissoR"
    print("Computer choice is \n", comp_choice_name)
    
    print(choice_name,'Vs',comp_choice_name)
    
    # Checking for Draw
    if choice == comp_choice:
        print('Its a Draw',end="")
        result="DRAW"
        
    # Checking for Winning
    if (choice == 1 and comp_choice == 2):
        print('paper wins =>',end="")
        result = 'papeR'
    elif (choice == 2 and comp_choice == 1):
        print('paper wins =>',end="")
        result ='Paper'
    
    if (choice == 1 and comp_choice == 3):
        print('Rock wins =>\n',end="")
        result ='Rock'
    elif (choice == 3 and comp_choice == 1):
        print('Rock wins =>\n',end="")
        result ='rocK'
    if (choice==2 and comp_choice==3):
        print('Scissors wins =>',end="")
        result='scissoR'
    elif (choice==3 and comp_choice==2):
        print('Scissors wins =>',end="")
        result='Scissors'
    
    #Printing the winner
    if result == 'DRAW':
        print("<== Its a tie ==>")
    elif result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
    
    print("Do you want to play again? (Y/N)")
    ans = input()
    if ans.lower() != "y":
        break
print("thanks for playing")
