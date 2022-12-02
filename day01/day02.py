import elves_data
elves = elves_data.data.split("\n\n")
record = []
for elf in elves:
    s = 0
    for cal in elf.split("\n"): s += int(cal)
    record.append(s)
record.sort()
print(sum(record[len(record)-3:len(record)]))