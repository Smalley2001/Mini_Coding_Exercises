# Write a program that uses nested loops to draw this pattern
# *******
# ******
# *****
# ****
# ***
# **
# *

for i in range(7,0,-1):
  for n in range(i,0,-1):
    print("*", end="")
  print()