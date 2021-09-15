import ctypes
import subprocess
from platform import system


def windowsCommand(command):
    ctypes.windll.winmm.mciSendStringW(
        command, ctypes.create_unicode_buffer(600), 559, 0)


if system() == "Windows":
    def play(fileName):
        windowsCommand("open " + fileName)
        windowsCommand("play " + fileName + " wait")
        windowsCommand("close " + fileName)
elif system() == "Darwin":
    def play(fileName):
        subprocess.Popen("exec afplay \'" + fileName+"\'", universal_newlines=True,
                         shell=True, stdout=-1, stderr=-1).communicate()
elif system() == "Linux":  # only works for wav files, otherwise plays white noise
    def play(fileName):
        subprocess.Popen("exec aplay --quiet " + fileName, universal_newlines=True,
                         shell=True, stdout=-1, stderr=-1).communicate()
