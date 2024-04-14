import datetime
import os

output = open("manual ID logs.txt","w")
source = open("LogOutput.log", encoding="utf8")

# logfile modification timestamp
modification_timestamp = os.path.getmtime("LogOutput.log")
# convert timestamp into DateTime object
modification_datetime = datetime.datetime.fromtimestamp(modification_timestamp)
output.write(str(modification_datetime)+"\n"+"\n")

for line in source:
    if "Steam User" in line:
        #JUST THE NUMBERS
        line = line.strip().split(' ')
        output.write(str(line[13]) + '\n')
        
        #COMPLETE LINES
        #output.write(str(line) + '\n')