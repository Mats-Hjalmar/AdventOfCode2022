import elves_data
elves = elves_data.data.split("\n\n")
record = 0
for elf in elves:
    s = 0
    for cal in elf.split("\n"): s += int(cal)
    if record < s: record = s
print(record)
