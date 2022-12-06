#advent of code
#day 6
f = open("6_input_file", "r") #read input file
content = list(f.read())

def solution(needed_length):
    for i in range(len(content)-needed_length):
        solution_check = True
        current_window = content[i:i+needed_length]
        current_window.sort()
        for cha_ind in range(len(current_window)-1):
            if current_window[cha_ind] == current_window[cha_ind+1]:
                solution_check = False
                break
        if solution_check == True:
            return(i+needed_length)

print("part 1", solution(4))
print("part 2", solution(14))
