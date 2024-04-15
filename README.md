# Stick-Fight-the-Game-Steam-ID-logger
A bunch of python files to automatically store the Steam IDs of people you played Stickfight with.

So far I only made the scripts to work on my own computer, maybe I'll make a more compatible version someday.

# What you need for the setup
-  probably only runs on Windows
-  Python 3.9.13
    -  possibly just any version of python 3.X
    -  you might have to install one or two modules
-  BepInEx
    -  BepInEx.cfg: "UnityLogListening = true"
    -  BepInEx.cfg: "WriteUnityLog = true"
    -  BepInEx.cfg: "AppendLog = false"
-  You gotta get used to only opening the game via desktop shortcut for it to be automatic.

# The setup
1. Dump all the files directly in your StickFightTheGame - BepInEx folder. (it's where "LogOutput.log" will generate)
2. Make a desktop shortcut for "Stick Fight the Game.bat" and use only that shortcut to start the game. (It stores the IDs from last session and then starts the game, which will reset "LogOutput.log")
3. Make sure .py files by default open with Python.
4. If stuff just won't work, check if your text files get encoded differently than "utf8".
