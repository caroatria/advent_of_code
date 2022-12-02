#advent of code 1st of december
f = open("1_input_file", "r")
content = f.readlines()

curr_cal = 0
max_cal = 0
i=1

max_list = []
for line in content:
    if line == "\n":
        i+=1
        max_list.append(curr_cal)
        curr_cal = 0
    else:
        curr_cal += int(line)
        if curr_cal > max_cal:
            max_cal = curr_cal
            max_elf = i
        if content.index(line) == len(content)-1:
            max_list.append(curr_cal)

summed_cals = 0
for i in range(3):
    max_val = max(max_list)
    summed_cals += (max_val)
    max_list.remove(max_val)

print("maximum",max_cal,"carried by elf",max_elf)
print("the three elves with the most calories are carrying",summed_cals,"in sum.")
