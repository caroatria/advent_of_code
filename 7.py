#advent of code
#december 7th

from collections import defaultdict 
def main():
    lines = map(str.split,open("7_input_file").read().splitlines())
    path,dirs = [], defaultdict(int)

    for line in lines:
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "..":
                    path.pop()
                else:
                    path.append(line[2])
        elif line[0] != "dir":
            for i in range(len(path)):
                dirs[tuple(path[:i+1])] += int(line[0])
    print("solution part 1",sum(size for size in dirs.values() if size <= 100000))

    required = 30000000 - (70000000 - dirs[("/",)])

    print("",min(size for size in dirs.values() if size >= required))

if __name__ == "__main__":
    main()
