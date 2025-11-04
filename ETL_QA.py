'''
lst = [1,2,3,4,5]
print (lst)
cnt= 0
for i in lst:
    print (i)
    cnt += i

print("Sum of elements in the list:",cnt)

sum_lst = sum(lst)
print(sum_lst)
'''
'''
my_list = [6,1,2,3,4,5]
a = my_list[0]
print(a)
for i in my_list[1:]:
    if i > a:
        a = my_list[i]

print("Larget element is:",a)

l = max(my_list)
print(l)
'''
'''
my_list = [6,1,2,3,1,2,6]
sort_list = sorted(my_list)
print(my_list)
u_list = []
un_list = []
for i in my_list:
    if i not in u_list:
        u_list.append(i)
    else:
        un_list.append(i)

print(u_list)
print(un_list)


my_list = [6,1,2,3,1,2,7,8]
my_list.sort(reverse=True)
sort_list = sorted(my_list)
print(sort_list)
l = len(sort_list)
sec_lar = sort_list[l-2]
print(sec_lar)



org_str = 'arjuna'
print(org_str.replace('a','b',1))


def dup_list(my_list):
    dup_list = []
    unq_list = []
    for i in my_list:
        if i not in unq_list:
            unq_list.append(i)
        else:
            dup_list.append(i)
    return unq_list

my_list = [1,2,3,4,5,6,1,2,7]
ans_list = dup_list(my_list)
print(ans_list)
print(dup_list([1,2,3,4,5,6,1,2]))

'''

'''
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = []
for item in my_list:
    if item not in unique_elements:
        unique_elements.append(item)
print(unique_elements)


my_list = [1, 2, 2, 3, 4, 4, 5]
uniq = set(my_list)
print(uniq)
'''

import pandas as pd

df = pd.read_csv("emp.csv")



print(df.loc[7]g)

print(1+2)








