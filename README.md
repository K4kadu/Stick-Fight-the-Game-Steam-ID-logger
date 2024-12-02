# Stick-Fight-the-Game-Steam-ID-logger
A bunch of python files to automatically store the Steam IDs of people you played Stickfight with.
These scripts aren't made with compatability or user friendliness in mind, so sorry in advance.

# What you need for the setup
-  might only run on Windows
-  any version of Python 3
-  BepInEx
-  You gotta get used to only opening the game via desktop shortcut for it to be automatic.

# The setup
1. Once you have BepInEx installed, go to ./BepInEx/config/BepInEx.cfg and apply the following settings:
    -  BepInEx.cfg: "UnityLogListening = true"
    -  BepInEx.cfg: "WriteUnityLog = true"
    -  BepInEx.cfg: "AppendLog = false"
3. Dump all the files directly in your ./StickFightTheGame/BepInEx folder. (it's where "LogOutput.log" will generate)
4. Make a desktop shortcut for "Stick Fight the Game.bat" and use only that shortcut to start the game. (It stores the IDs from last session and then starts the game, which will reset "LogOutput.log")
5. Make sure .py files by default open with Python.
