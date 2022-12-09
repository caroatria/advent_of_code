#advent of code
#december 9th
from itertools import product

#['R4', 'U4', 'L3', 'D1', 'R4', 'D1', 'L5', 'R2']

direction_dict = {"U":(0,1),"D":(0,-1),"R":(1,0),"L":(-1,0)}

f = open("9_input_file", "r") #read input file
content = f.read().split("\n")
content = content[:len(content)-1]
# print(content)

starting_pos = (0,0)
new_tail_position = starting_pos

already_visited = []

def tail_movement(current_pos,input_direction,tail_position): 
    # print("current head position",current_pos)
    # print("current tail position",tail_position)
    addx,addy = direction_dict[input_direction]
    x = current_pos[0] + addx
    y = current_pos[1] + addy
    new_position = (x,y)
    #print("new head position",new_position)

    if abs(new_position[0]-tail_position[0]) <= 2 and abs(new_position[1]-tail_position[1]) <= 2:
        moves = list(product([tail_position[0]-1, tail_position[0]+1],[tail_position[1],tail_position[1]]))+ list(product([tail_position[0],tail_position[0]],[tail_position[1]-1,tail_position[1]+1]))
        moves = [(tail_x,tail_y) for tail_x,tail_y in set(moves) if abs(tail_x-x)< 2 and abs(tail_y-y) <2] #and tail_x >= 0 and tail_y >= 0
        #print("2 points away. make 1 step in this direction")
        new_tail_position = moves[0]
    elif abs(new_position[0]-tail_position[0]) == 1 or abs(new_position[1]-tail_position[1]) == 1:
        # #print("1 position away. stay there") #change nothing
        new_tail_position = tail_position
    elif new_position == tail_position:
        # #print("same spot") #change nothing
        new_tail_position = tail_position
    else:
        #print("tail not touching head anymore! move diagonally")
        moves = list(product([tail_position[0]-1, tail_position[0]+1],[tail_position[1],tail_position[1]]))+ list(product([tail_position[0],tail_position[0]],[tail_position[1]-1,tail_position[1]+1]))
        moves = [(tail_x,tail_y) for tail_x,tail_y in set(moves) if abs(tail_x - x) <= 1 and abs(tail_y - y) <= 1]
        new_tail_position = moves[0]

    # #print("new tail position",new_tail_position)
    return(new_position,new_tail_position)


for row in content:
    row_list = row.split(" ")
    direc = row_list[0]
    factor = int(row_list[1])
    for i in range(factor):
        # #print("\n")
        starting_pos,new_tail_position = tail_movement(starting_pos,direc,new_tail_position)
        #print(new_tail_position)
        already_visited.append(new_tail_position)

already_visited.append(starting_pos)
print("solution part 1", len(set(already_visited)))