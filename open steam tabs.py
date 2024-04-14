import subprocess
import os

source = open("LogOutput.log", encoding="utf8")
duplicate = False
list = []

for line in source:
    if "Steam User" in line:
        line = line.strip().split(' ')
        if str(line[13]) != "User:":
            for i in list:
                if i == str(line[13]):
                    duplicate = True
                    break
            if duplicate == False:
                list.append(str(line[13]))
            else:
                duplicate = False

for i in list:
    open("open_IDs.bat","a").write("Start https://steamcommunity.com/profiles/" + str(i) + '\n')
subprocess.run([r"open_IDs.bat"])
os.remove("open_IDs.bat")