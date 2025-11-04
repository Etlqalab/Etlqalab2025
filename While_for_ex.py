'''
for i in "supercalifragilisticexpialidocious":
    print(i)
'''

'''
word = "supercalifragilisticexpialidocious"
num = 0
while num < len(word) + 1:
    print(word[num])
    num += 1
'''
'''
for num in range(100,142,2):
    print(num)
    num += 2

num = 100
while num <= 140:
    print(num)
    num += 2


word = 'My name is Arjun'
for char in word:
    print(char)
    if char == 'n':
        continue
'''

dice = int(input("How many dice are you rolling? "))
side = int(input("How many sides on each dice? "))

from random import randint

x = 1

while True:
    result = "|"
    for x in range(dice):
        rand = randint(1,side)
        result += f"{rand}|"
    print(result)
    reply = input(f"roll again? ('q' to quit)")
    if reply == 'q':
        break




