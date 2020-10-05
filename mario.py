from cs50 import get_string
import re

while True:
    h = get_string("Height: ")
    if re.search("^[1-8]$", h):
     #   print("height is between 1-8")
        h = int(h)
        break
for i in range(h):
    for j in range(1, h-i):
        print(" ", end="")
    for k in range(i+1):
        print("#", end="")
    print("  ", end="")
    for l in range(i+1):
        print("#", end="")
    print("\n", end="")