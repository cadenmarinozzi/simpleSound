import ctypes

def windowsCommand(command):
    ctypes.windll.winmm.mciSendStringW(command, ctypes.create_unicode_buffer(600), 559, 0);

def play(fileName):
    windowsCommand("open " + fileName);
    windowsCommand("play " + fileName + " wait");
    windowsCommand("close " + fileName);
