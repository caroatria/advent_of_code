#advent of code
#december 4th
f = open("4_input_test", "r") #read input file
content = f.readlines()
# print("content",content)

part_1_section_overlap = 0
part_2_section_overlap = 0
for row in content:
    row = row.split(",")
    elf_1 = row[0].strip("\n").split("-")
    elf_1_start,elf_1_stop = int(elf_1[0]),int(elf_1[1])
    elf_2 = row[1].strip("\n").split("-")
    elf_2_start,elf_2_stop = int(elf_2[0]),int(elf_2[1])
    if elf_1_start <= elf_2_start and elf_1_stop >= elf_2_stop:
        part_1_section_overlap += 1
    elif elf_2_start <= elf_1_start and elf_2_stop >= elf_1_stop:
        part_1_section_overlap += 1
    if elf_1_start <= elf_2_start <= elf_1_stop:
        part_2_section_overlap += 1
    elif elf_2_start <= elf_1_start <= elf_2_stop:
        part_2_section_overlap += 1


print("solution part 1",part_1_section_overlap)
print("solution part 2",part_2_section_overlap)

