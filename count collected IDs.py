import os

source = open("automatic ID logs.txt", encoding="utf8")
duplicate = False
list = []

for line in source:
    if "7656119" in line:
        for i in list:
            if i == line:
                duplicate = True
                break
        if duplicate == False:
            list.append(line)
        else:
            duplicate = False
            
print('You have collected ' + str(len(list)) + ' indiviual IDs and should probably get a hobby.')
input()