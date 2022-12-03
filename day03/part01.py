from rhucksack_input import puzzle_input

def char_to_int(c):
    if (c.islower()): return ord(c) - ord("a") + 1
    return ord(c) - ord("A") + 1 + 26

result = 0
for rhuck in puzzle_input.split("\n"):
    for x in set(rhuck[0:int(len(rhuck)/2)]).intersection(rhuck[int(len(rhuck)/2):len(rhuck)]):
        result += char_to_int(x)
print(result)