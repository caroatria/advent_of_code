#advend of code
#december 3rd




character_scores = {"a":1,"A":27}

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

def string_intersection(str1,str2):
    res = ""
    for i in str1:
        if i in str2 and not i in res:
            res += i
    return(res)

f = open("3_input_file", "r")
content = f.readlines()
# print(content)
common_character = []
for line in content:
    mid = int(len(line)/2-0.5) #mid point to separate compartments
    first_comp = (line[0:mid])
    second_comp = (line[mid:len(line)])
    common_character.append(string_intersection(first_comp,second_comp))

    
sum_of_chars = 0
for char in common_character:
    sum_of_chars += character_scores[char]
print(sum_of_chars)

