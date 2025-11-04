marks = {'Arjun' : 25,
          'Dinya' : 50,
          'Aadya' : 75,
          'Family' : 90}

for name in marks.keys():
    print(name)

for score in marks.values():
    print(score)

for item in marks.items():
    print(item)

for k,v in marks.items():
    print(k,v)

max_score = 0
max_name = ''

for name,score in marks.items():
    if score > max_score:
        max_score = score
        max_name = name

print(f"the highest mark {max_score} is got by the student {max_name}")



