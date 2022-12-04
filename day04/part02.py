from section_input import sections

result = 0

for x in sections.split("\n"):
    nums = (int(x.split(",")[0].split("-")[0]), int(x.split(",")[0].split("-")[1]), int(x.split(",")[1].split("-")[0]), int(x.split(",")[1].split("-")[1]))
    p1 = range(nums[0], nums[1] + 1)
    p2 = range(nums[2], nums[3] + 1)
    if len(set(p1).intersection(set(p2))) >= 1:
        result += 1
        
print(result)
