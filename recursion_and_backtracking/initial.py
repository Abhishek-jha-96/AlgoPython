"""
The Towers of Hanoi is a mathematical puzzle. It consists of three rods (or pegs or towers) and a 
number of disks of different sizes which can slide onto any rod. The puzzle starts with the disks on one rod in 
ascending order of size, the smallest at the top, thus making a conical shape. The objective of the puzzle is to 
move the entire stack to another rod, satisfying the following rules: 
• Only one disk may be moved ut a time. 
• Each move consists of taking the upper disk from one of the rods and sliding it onto another rod, on top 
of the other disks that may already be present on that rod. 
• No disk may be placed on top of a smaller disk. 
"""
def tower_of_hanoi(n, start=1, end=3):
    if n:
        tower_of_hanoi(n-1, start, 6-start-end)
        print("Move disk from {} to {}".format(start, end))
        tower_of_hanoi(n-1, 6-start-end, end)

tower_of_hanoi(5)