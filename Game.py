print("WELCOME 🙏")
import random
comp_wins = 0
user_wins = 0
def game(comp, user):
    global comp_wins
    global user_wins
    if (comp == user):
        comp_wins=comp_wins+0
        user_wins=user_wins+0
    elif (comp == "P"):
        if (user == "R"):
            comp_wins = comp_wins + 1
        elif (user == "S"):
            user_wins = user_wins + 1

    elif (comp == "R"):
        if (user == "P"):
            user_wins = user_wins + 1
        elif (user == "S"):
            comp_wins = comp_wins + 1

    elif (comp == "S"):
        if (user == "P"):
            comp_wins = comp_wins + 1
        elif (user == "R"):
            user_wins = user_wins + 1
    print("Rounds won by computer:",comp_wins)
    print("Rounds won by user:",user_wins)
    if (comp_wins > user_wins):
        print("Computer is leading by☹:",comp_wins-user_wins)
    elif(comp_wins < user_wins):
        print("User is leading by😊:",user_wins-comp_wins)
    elif(comp_wins == user_wins):
        print("No one is leading")
    if(j==d):
        if(comp_wins>user_wins):
            print("computer won by☹:",comp_wins-user_wins)
        elif(user_wins>comp_wins):
            print("user won by☺:",user_wins-comp_wins)
        else:
            print("it's a tie")
print("Let's play rock(R),paper(P) and scissor(S) game!!!")
j = int(input("Enter number of rounds you want to play:"))
for d in range(1, j+1):
    user = input("user's turn rock(R) paper(P) scissor(S):")
    print("comp's turn rock(R) paper(P) scissor(S):", end="")
    comprand = random.randint(1, 3)
    if (comprand == 1):
        comp = "R"
    elif (comprand == 2):
        comp = "P"
    elif (comprand == 3):
        comp = "S"
    print(comp)
    if(user=="R" or user=="P" or user=="S"):
        game(comp, user)
    else:
        print("enter valid input")
        game(comp, user)
    if (d == j):
        print(j,"rounds compeleted\nEnd game\nThank You for playing!!!!")
        break