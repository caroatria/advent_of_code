#advent of code
#december 10th

f = open("10_input_file","r")
content = f.read().split("\n")
content = content[:len(content)-1]

signal_points = list(20 + 40* i for i in range(6))
old_sum = 0
possible_sums = []

def sum_signal_strength(new_sum):
    global old_sum
    old_sum += new_sum
    global possible_sums
    possible_sums.append(old_sum)
    return()


def check_signal(cycle_nr,X):
    # print("cycle NR",cycle_nr)
    strength = cycle_nr * X
    sum_signal_strength(strength)
    return(strength)

def program_reader(command,cycle_nr,X):
    if command == "noop": #takes 1 cycle, no effect
        cycle_nr += 1
        if (cycle_nr in signal_points):
            check_signal(cycle_nr,X)
    elif command.split(" ")[0] == "addx": #takes 2 cycles, add nr
        value = int(command.split(" ")[1])
        cycle_nr += 1 #nothing happens
        if (cycle_nr in signal_points):
            check_signal(cycle_nr,X)
        cycle_nr += 1 #nothing happens
        # if (cycle_nr in signal_points):
        #     check_signal(cycle_nr,X)
        X += value
        if (cycle_nr in signal_points):
            check_signal(cycle_nr,X)

    return(cycle_nr,X)

def commands(i,cycle_nr,X):
    if i < len(content):
        command = content[i]
        # print(cycle_nr,X)
        new_cylce_nr,new_X = program_reader(command,cycle_nr,X)
        i += 1
        commands(i,new_cylce_nr,new_X)


commands(0,1,1)


print("solution part 1",possible_sums[len(possible_sums)-1])