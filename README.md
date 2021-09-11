# simpleSound
A very very very simple sound playing library for windows.

Documentation:
```
SimpleSound:
  play(fileName); -> if the file doesn't exist it returns: fileName + " could not be found";
```

Installation:
```
pip/3 install simpleSound

example:
pip install simpleSound
pip3 install simpleSound

```

Example Usage:
```Python
from simpleSound import SimpleSound

simpleSound = SimpleSound();
simpleSound.play("Sound.mp3");
```
