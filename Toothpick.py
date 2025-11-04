player1 = input("enter player 1's name: ")
player2 = input("enter player 2's name: ")
count = 13

toothpick = "|"
print("| " * count)
print(f"There are {count} toothpick left")

while count > 0:
    p1 = int(input(f"How many do you take, {player1} ? "))
    if p1 != 1 and p1 != 2 and p1 != 3:
        p1 = int(input("You can only input 1, 2 or 3"))
    count -= p1
    print("| " * count)

    if count <= 0:
        print(f"{player1} wins!!!")
        print("GAME OVER!!!")
        break
    print(f"There are {count} toothpick left")

    p2 = int(input(f"How many do you take, {player2} ? "))
    count -= p2
    print("| " * count)

    if count <= 0:
        print(f"{player2} wins!!!")
        print("GAME OVER!!!")
        break
    print(f"There are {count} toothpick left")












