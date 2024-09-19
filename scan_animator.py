import sys
import time

def animated_print(text, delay=0.1):
   try:
     for char in text:
         sys.stdout.write(char)
         sys.stdout.flush()
         time.sleep(delay)
   except KeyboardInterrupt:
         pass
if len(sys.argv) > 1:
      target = sys.argv[1]
      text = f"\033[1;34mstart scanning on \033[1;31m{target}\033[0m\033[0m"
      animated_print(text)
else: 
      pass
