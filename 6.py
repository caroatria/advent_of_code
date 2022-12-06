#advent of code
#day 6

f = open("6_input_file", "r") #read input file
content = f.read()
print("content:",content)

id_code = ""
for char in content:
        if char not in id_code:
            if len(id_code) == 4:
                break
            elif len(id_code)<4:
                id_code += char
        else:
            id_code = ""
print("code",id_code)
print("solution part 1",content.index(id_code)+3)
