from rhucksack_input import puzzle_input
import numpy as np

def char_to_int(c):
    if (c.islower()): return ord(c) - ord("a") + 1
    return ord(c) - ord("A") + 1 + 26

result = 0
rhucksacks = puzzle_input.split("\n")
for trioRhuck in np.reshape(rhucksacks, (int(len(rhucksacks)/3), 3)):
    commonChars = []
    for x in trioRhuck[0]:
        if x in trioRhuck[1]:
            if x in trioRhuck[2]:
                commonChars.append(x)
    result += char_to_int(commonChars[0])
print(result)