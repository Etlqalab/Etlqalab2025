'''
def replace(word,rep='-'):
    print(word.upper().replace("A", rep))





replace("My name is arjun")
replace("My name is arjun","/")


def laugh(time=20):
    print("HA" * time)

laugh(10)
laugh()

def greet(person,msg='Hi'):
    print(f"{person} {msg}")

greet("Arjun")
'''

'''
def zoo_out():
    animal = "cat"
    print("The animal one is :", animal)
    def zoo_in():
        print("The animal in is :", animal)
    zoo_in()

zoo_out()
'''
colour = 'purplr'
def my_fun():
    global colour
    colour = 'green'

print(colour)
my_fun()
print(colour)



