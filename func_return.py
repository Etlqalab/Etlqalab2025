def average(*arg):
    total = 0
    for i in arg:
        total+= i
    avg = total/len(arg)
    return avg

average(1,2,3,4,5)

def print_ages(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} is {v} year old")

print_ages(arjun=36,dinya=25,Aadya=6)