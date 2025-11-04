

import random

roll1 = random.randint(1,6)
roll2 = random.randint(1,6)

rollcnt = 1

while roll1 !=1 or roll2 != 1:
    print(roll1,roll2)
    rollcnt += 1
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)

print(roll1,roll2)
print("YAY SNAKE EYE")
print(f"It took {rollcnt} time to roll")
