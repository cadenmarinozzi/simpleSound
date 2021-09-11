import ctypes

def windowsCommand(command):
    buffer = ctypes.create_unicode_buffer(600);
    ctypes.windll.winmm.mciSendStringW(command, buffer, 559, 0);

def play(fileName):
    windowsCommand("open " + fileName);
    windowsCommand("play " + fileName + " wait");
    windowsCommand("close " + fileName);
