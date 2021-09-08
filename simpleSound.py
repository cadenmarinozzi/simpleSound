import os, ctypes

def windowsCommand(command):
    buffer = ctypes.create_unicode_buffer(600);
    ctypes.windll.winmm.mciSendStringW(command, buffer, 559, 0);

class SimpleSound():
    def play(self, fileName):
        if (os.path.isfile(fileName)):
            windowsCommand("open " + fileName);
            windowsCommand("play " + fileName + " wait");
            windowsCommand("close " + fileName);
        else:
            print(fileName + " could not be found.");
