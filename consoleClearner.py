import os
import platform
command = "clear" if platform.system() == "Linux" else "cls"
clear = lambda: os.system(command)

def cleanConsole():
    return clear()