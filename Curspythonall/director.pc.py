#context manager - libraria os (operating system=window,linux)
#search de fisiere

import os

with os.scandir("C:\\Users\\MyPC\\Desktop") as entries:   #afisare director curent
     for entry in entries:
          print(entry.name, "->", entry.stat().st_size, "bytes")