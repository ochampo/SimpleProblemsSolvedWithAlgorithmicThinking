#
#There are 100 doors in a row, all doors are initially closed. \
#A person walks through all doors multiple times and toggle 
#(if open then close, if close then open) them in the following way: 
#
doors  = [False] * 101

print(doors)

for i in range(1, 101):
    doors[i] = not doors[i]