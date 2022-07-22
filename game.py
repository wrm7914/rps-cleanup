



from random import choice
valid_choices = ["rock", "paper", "scissors"]
#
# USER SELECTION
#

# ONLY run this code if we run script from the command line
# But not if we are importing some code from this file to another file
# prevents execution of code below when all we want to do is import test/funciton in isolation


def winner(user_choice, computer_choice):
    return u == "rock" and c == "rock":
        #print("It's a tie!")
        return("It's a tie!")
    elif u == "rock" and c == "paper":
        #print("The computer wins")
        return("The computer wins")
    elif u == "rock" and c == "scissors":
        #print("The user wins")

    elif u == "paper" and c == "rock":
        #print("The computer wins")
    elif u == "paper" and c == "paper":
        #print("It's a tie!")
    elif u == "paper" and c == "scissors":
        #print("The user wins")

    elif u == "scissors" and c == "rock":
        #print("The computer wins")
    elif u == "scissors" and c == "paper":
        #print("The user wins")
    elif u == "scissors" and c == "scissors":
        #print("It's a tie!")


if __name__ == "__main__":

    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in valid_choices:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(valid_choices)
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #

    if u == "rock" and c == "rock":
        print("It's a tie!")
    elif u == "rock" and c == "paper":
        print("The computer wins")
    elif u == "rock" and c == "scissors":
        print("The user wins")

    elif u == "paper" and c == "rock":
        print("The computer wins")
    elif u == "paper" and c == "paper":
        print("It's a tie!")
    elif u == "paper" and c == "scissors":
        print("The user wins")

    elif u == "scissors" and c == "rock":
        print("The computer wins")
    elif u == "scissors" and c == "paper":
        print("The user wins")
    elif u == "scissors" and c == "scissors":
        print("It's a tie!")
