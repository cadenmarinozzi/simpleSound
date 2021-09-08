# simpleSound
A very very very simple sound playing library.

Documentation:
```
SimpleSound:
  play(fileName); -> if the file doesn't exist it returns: fileName + " could not be found";
```

Example Usage:
```Python
from simpleSound import SimpleSound

simpleSound = SimpleSound();
simpleSound.play("Sound.mp3");
```
