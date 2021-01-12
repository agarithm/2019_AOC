
def get_addr(x):
    line = x // 4
    pos = x % 4
    return line,pos

def run_prog(prog):
    for cmd in prog:
        if len(cmd) < 4:
            return prog
        #get the operands
        line,pos = get_addr(cmd[1])
        a = prog[line][pos]
        line,pos = get_addr(cmd[2])
        b =  prog[line][pos]
        if cmd[0] == 1:
            val = a + b
        elif cmd[0] == 2:
            val = a * b
        else:
            return prog

        #set the value
        line,pos = get_addr(cmd[3])
        prog[line][pos]=val
            
        
def hunt_noun_verb(x,line):

    print(f"{prog[0]} {prog[1]} {prog[2]}")
    for noun in range(0,100,1):
        for verb in range(0,100,1):
            new_prog = parse_prog(line)
            new_prog[0][1] = noun
            new_prog[0][2] = verb

            print(f"{noun} {verb} {new_prog[0]} {new_prog[1]} {new_prog[2]}")
            new_prog = run_prog(new_prog)
            print(f"{noun} {verb} {new_prog[0]} {new_prog[1]} {new_prog[2]}\n")
            if new_prog[0][0] == x:
                return noun,verb;


def parse_prog(line):
        #build a Program
        data = line.split(",")
        data = list(map(int,data))
        prog = []
        while len(data):
            prog.append(data[:4])
            data = data[4:]
        return prog

with open("data/prog_int_code") as f:
    for line in f:
        prog = parse_prog(line)
        prog[0][1] = 12
        prog[0][2] = 2
        state = run_prog(parse_prog(line))
        print(state)

        noun,verb = hunt_noun_verb(19690720,line)
        print(f"NOUN = {noun}, VERB = {verb}, ANSWER = {100*noun+verb}")
