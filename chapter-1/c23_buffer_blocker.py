buffer = [1, 2]
try:
 buffer[3] = 3
except IndexError:
  print("Don't try buffer overflow attacks in Python!")