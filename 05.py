

def run_prog(listing):
    listing = listing.strip();
    prog = listing.split(",");

    def get_command(ic):
        nonlocal prog
        return prog[ic].zfill(5);

    def get_opcode(cmd):
        return cmd[3:]

    def get_params_and_modes(cmd):
        nonlocal prog
        nonlocal ic
        a_mode = int(cmd[2])
        b_mode = int(cmd[1])
        c_mode = int(cmd[0])
        a = get_addr(ic+1) if ic+1 < len(prog) else 0
        b = get_addr(ic+2) if ic+2 < len(prog) else 0
        c = get_addr(ic+3) if ic+3 < len(prog) else 0
        print(f"IC = {ic} -- {cmd}, {a}, {b}, {c}")
        return a, b, c, a_mode, b_mode, c_mode

    def get_input():
        val = input("#: ")
        return int(val)

    def get_addr(addr,mode=0):
        nonlocal prog
        return addr if mode else int(prog[addr])


    def set_addr(addr,val):
        nonlocal prog
        prog[addr]=f"{val}"
        return

    def output(val):
        print(f"{val}")
        return


    done = False
    ic = 0;
    while not done:
        cmd = get_command(ic)
        op = get_opcode(cmd);
        a, b, c, a_mode, b_mode, c_mode = get_params_and_modes(cmd);
        if op == "01":                              #ADD
            a = get_addr(a,a_mode)
            b = get_addr(b,b_mode)
            set_addr(c,a+b)
            ic += 4
        elif op == "02":                            #MULTIPLY
            a = get_addr(a,a_mode)
            b = get_addr(b,b_mode)
            set_addr(c,a*b)
            ic += 4
        elif op == "03":                            #INPUT
            set_addr(a,get_input())
            ic += 2
        elif op == "04":                            #OUTPUT
            output(get_addr(a,a_mode))
            ic += 2
        elif op == "05":                            #JMP if TRUE
            a = get_addr(a,a_mode)
            b = get_addr(b,b_mode)
            ic = b if a else ic+3
        elif op == "06":                            #JMP if FALSE
            a = get_addr(a,a_mode)
            b = get_addr(b,b_mode)
            ic = b if a==0 else ic+3
        elif op == "07":                            #LT
            a = get_addr(a,a_mode)
            b = get_addr(b,b_mode)
            set_addr(c, 1 if a<b else 0 )
            ic += 4
        elif op == "08":                            #EQ
            a = get_addr(a,a_mode)
            b = get_addr(b,b_mode)
            set_addr(c, 1 if a==b else 0 )
            ic += 4
        else:
            done = True

        if ic >= len(prog):
            done = True

    return prog


def parse_prog(line):
        #build a Program
        return line.split(",")

with open("data/diagnostics") as f:
    for line in f:
        print(run_prog(line))


