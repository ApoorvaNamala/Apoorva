# Enter your code here. Read input from STDIN. Print output to STDOUT
"""def wordcount(n, string):
    count = 0
    newlist = []
    for i in string:
        if i not in newlist:
            newlist.append(i)
    unique = len(newlist)
    print(unique)
    for i in newlist:
        count = 0
        for j in string:
            if i == j:
                count = count + 1
        print(count,end=" ")

n = int(input())
string = []
for i in range(0, n):
    str = input()
    string.append(str)
if n<= 10**5 :
    wordcount(n, string)"""

from collections import OrderedDict
#define empty ordered dictionary, which counts occurences
dict = OrderedDict()

for i in range(int(input())):
    #If input not in the dictionary, then add it
    #else increment the counter
    key = input()
    if not key in dict.keys():
        dict.update({key : 1})
        continue
    dict[key] += 1

print(len(dict.keys()))
print(*dict.values())

