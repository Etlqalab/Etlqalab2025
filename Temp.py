
your_move = input("enter your move: ").lower()
print(f"YOUR MOVE IS \n {your_move}")

print("COMPUTER MOVE IS")
from random import randint
comp_move = randint(1,3)

if comp_move == 1:
    print("rock")
    computer_move = "rock"
elif comp_move == 2:
    print("scissor")
    computer_move = "scissor"
else:
    print("paper")
    computer_move = "paper"

if your_move == computer_move:
    print("IT'S A TIE")
elif your_move == 'paper' and comp_move == 1:
    print("YOU WIN")
elif your_move == 'rock' and comp_move == 2:
    print("YOU WIN")
elif your_move == 'scissor' and comp_move == 3:
    print("YOU WIN")
else:
    print("COMPUTER WIN")






