'''def contain_pickle(*args):
    return 'pickle' in args

contain_pickle("red",45)
'''
'''
def count_fails(*args):
    cnt = 0
    for item in args:
        if item <= 50:
            cnt+= 1

    print(cnt)

count_fails(85,78,91)
'''
def get_top_students(**students):
    lst_std = []
    for k,v in students.items():
        if v >= 90:
            lst_std.append(k)

    print(lst_std)

get_top_students(stacy=83,             jim=69)



