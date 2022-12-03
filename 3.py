#advend of code
#december 3rd

f = open("3_input_file", "r") #read input file
content = f.readlines()

character_scores = {"a":1,"A":27} #stores values for each character of the alphabet
start_cha = "a"
for char in range(1,26):
    curr_char = chr(ord(start_cha)+char)
    character_scores[curr_char] = char+1
    curr_char = chr(ord(curr_char)+char)
    char += 1

start_cha = "A"
for char in range(27,52):
    curr_char = chr(ord(start_cha)+char-26)
    character_scores[curr_char] = char+1
    curr_char = chr(ord(curr_char)+char-26)
    char += 1

def string_intersection(str1,str2,str3="n/a"): #to get characters present in all strings
    res = ""
    if str3 == "n/a":
        for i in str1:
            if i in str2 and not i in res:
                res += i
    else:
        for i in str1:
            if i in str2:
                if i in str3 and i not in res:
                    res += i
    return(res)

common_character = []
for line in content:
    mid = int(len(line)/2-0.5) #mid point to separate compartments
    first_comp = (line[0:mid])
    second_comp = (line[mid:len(line)])
    common_character.append(string_intersection(first_comp,second_comp))

sum_of_chars = 0
for char in common_character:
    sum_of_chars += character_scores[char]
print("Items to rearrange",sum_of_chars) #solution part 1

common_character = []
start = 0
for index in range(int(len(content)/3)):
    current_group = content[start:start+3]
    start+=3
    first_elf = current_group[0].strip("\n")
    second_elf = current_group[1].strip("\n")
    third_elf = current_group[2].strip("\n")
    common_character.append(string_intersection(first_elf,second_elf,third_elf))

sum_of_chars = 0
for char in common_character:
    sum_of_chars += character_scores[char]
print("Groups of three elves:",sum_of_chars) #solution part 2