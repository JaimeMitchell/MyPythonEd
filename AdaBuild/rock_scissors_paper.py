rock = "rock"
scissors = "scissors"
paper = "paper"

game=[rock,scissors,paper]
game[0]

userChoice = str(input("User, please enter rock, scissors, or paper: "))
computerChoice = str(input("Computer, please enter rock, scissors, or paper: "))
if userChoice > computerChoice:
    print('you win')
elif computerChoice > userChoice:
    print('computer wins')
else:
    print('tie')
