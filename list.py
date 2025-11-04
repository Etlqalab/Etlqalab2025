
drivers = ["Charles", "Pierre", "Valterri", "Lewis", "George", "Lando"]
print(drivers)

drivers[2] = "Valtteri"
print(drivers)

drivers.append("Esteban")
print(drivers)

others = ["Blue", "Elton", "Colt"]
drivers.extend(others)
print(drivers)

drivers.remove("Colt")
print(drivers)

removed = drivers.pop(0)
print(removed)
print(drivers)

first = drivers.pop(0)
drivers.append(first)
print(drivers)

drivers.remove("Blue")
print(drivers)

drivers.remove("Elton")
drivers.insert(2,"Elton")
print(drivers)

podium = drivers[:3]
print(podium)

cnt = 1

for driver in drivers:
    print(cnt,driver,cnt)
    cnt += 1

'''
names = ['arjun','dinya','aadya']

for name in names:
    print("how are you", name)

idx = 0
while idx < len(names):
    print("I am fine", names[idx])
    idx += 1
'''



