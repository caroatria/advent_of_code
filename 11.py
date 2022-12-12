#advent of code
#december 11th

content = open("11_input_file","r").readlines()
from collections import defaultdict

monkey_dict = defaultdict(list)
monkey_interactions = defaultdict(int)
z=1
for i in range(0,len(content),7):
    current_monkey = int(content[i].strip(" \n :").split(" ")[1])
    current_items = (content[i+1].strip(" \n").split(":")[1])
    current_items = sorted(list(map(int,current_items.strip(" ").split(","))))
    z *= int(content[i+3].strip(" \n").split(" ")[3])
    monkey_dict[current_monkey] = current_items

for j in range(10000):
    for i in range(0,len(content),7):
        current_monkey = int(content[i].strip(" \n :").split(" ")[1])
        current_monkey = int(content[i].strip(" \n :").split(" ")[1])
        current_items = monkey_dict[current_monkey]
        inspecting = len(current_items)
        test = int(content[i+3].strip(" \n").split(" ")[3])
        if_true_throw = int(content[i+4].strip(" ").split(" ")[5])
        if_false_throw = int(content[i+5].strip(" ").split(" ")[5])
        monkey_dict[current_monkey] = current_items
        
        old_interaction = monkey_interactions[current_monkey]
        new_interaction = 0
        for old in current_items:
            new_interaction += 1
            monkey_dict[current_monkey] = []
            new_stress = eval(content[i+2].strip(" ")[17:30])
            new_stress = new_stress % z #for part 1 new_stress%3
            if new_stress%test == 0:
                if not monkey_dict[if_true_throw]:
                    monkey_dict[if_true_throw] = [new_stress]
                else:
                    monkey_dict[if_true_throw] = list(monkey_dict[if_true_throw]+ [new_stress])
                
            else:
                if not monkey_dict[if_false_throw]:
                    monkey_dict[if_false_throw] = [new_stress]
                else:
                    monkey_dict[if_false_throw] = list(monkey_dict[if_false_throw] + [new_stress])
        monkey_interactions[current_monkey] = new_interaction + old_interaction

           
values = list(monkey_interactions.values())
sorted_values = sorted(values)
x,y = (sorted_values[len(sorted_values)-2:len(sorted_values)])
print(sorted_values)
print("solution",x*y)


