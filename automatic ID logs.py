import datetime
import os

output = open("automatic ID logs.txt","a")
source = open("LogOutput.log", encoding="utf8")
list = []
duplicate = False

# logfile modification timestamp
modification_timestamp = os.path.getmtime("LogOutput.log")
# convert timestamp into DateTime object
modification_datetime = datetime.datetime.fromtimestamp(modification_timestamp)
output.write(str(modification_datetime)+"\n"+"\n")

for line in source:
    if "Steam User" in line:
        line = line.strip().split(' ')
        if str(line[13]) != "User:":
            for i in list:
                if i == str(line[13]):
                    print('duplicate found')
                    duplicate = True
                    break
            if duplicate == False:
                print('added ' + str(line[13]) + 'to the list')
                list.append(str(line[13]))
            else:
                print('reset duplicate variable')
                duplicate = False

for i in list:
    output.write(str(i) +'\n')
output.write('-----'+'\n'+'\n')