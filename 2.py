#advent of code
#december 2nd
f = open("2_input_file_cp", "r")
content = f.readlines()

score = 0
for line in content:
    if line == "\n":
        break
    f,s = line[0],line[2]
    if s == "X": #rock
        score += 1
        if f == "A": #draw
            score += 3
        elif f == "B": #you loose
            score += 0
        elif f == "C": #you win
            score += 6
    elif s == "Y": #paper
        score += 2
        if f =="A": #you win
            score += 6
        elif f == "B": #draw
            score += 3
        elif f == "C": #you loose
            score += 0
    elif s == "Z":
        score += 3
        if f =="A": #you loose
            score += 0
        elif f == "B": #you win
            score += 6
        elif f == "C": #draw
            score += 3

print("first score",score)

#second part
score = 0
for line in content:
    if line == "\n":
        break
    f,s = line[0],line[2]
    if s == "Z": #you need to win
        score += 6
        if f == "A": #you must play paper
            score += 2
        elif f == "B": #you must play scissors
            score += 3
        elif f == "C": #you must play rock
            score += 1
    elif s == "Y": #you need to end in draw
        score += 3
        if f =="A": #you must play rock
            score += 1
        elif f == "B": #you must play paper
            score += 2
        elif f == "C": #you must play scissors
            score += 3
    elif s == "X": ##you need to loose
        score += 0
        if f =="A": #you must play scissors
            score += 3
        elif f == "B": #you must play rock
            score += 1
        elif f == "C": #you must play
            score += 2

print("second score",score)

