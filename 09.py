
def run_prog(listing,ic=0,in_fifo=[],out_fifo=[]):
    listing = listing.strip();
    prog = listing.split(",");
    ram = {}
    rb = 0


    def get_command(ic):
        nonlocal prog
        return prog[ic].zfill(5);

    def get_opcode(cmd):
        return cmd[3:]

    def get_params_and_modes(cmd):
        nonlocal prog
        nonlocal ic
        nonlocal rb
        a_mode = int(cmd[2])
        b_mode = int(cmd[1])
        c_mode = int(cmd[0])
        a = get_addr(ic+1) if ic+1 < len(prog) else 0
        b = get_addr(ic+2) if ic+2 < len(prog) else 0
        c = get_addr(ic+3) if ic+3 < len(prog) else 0
        print(f"IC = {ic} {rb} -- {cmd}, {a}, {b}, {c}")
        return a, b, c, a_mode, b_mode, c_mode

    def get_input():
        nonlocal in_fifo;
        return int(in_fifo.pop(0))

    def read_ram(addr):
        key = f"{addr}"
        return prog[addr] if addr <len(prog) else ram[key] if key in ram else 0

    def get_addr(addr,mode=0):
        nonlocal prog
        if mode == 0:
            #ABS POS
            return int(read_ram(addr))
        elif mode == 1:
            #SELF
            return addr
        elif mode == 2:
            #REL POS
            return int(read_ram(rb+addr))
        else:
            print("ERROR: Unknown mode, returning 0")
            return 0


    def set_addr(addr,val,mode=1):
        nonlocal prog
        if mode == 2:
            addr += rb
        if addr < len(prog):
            prog[addr]=f"{val}"
        else:
            key = f"{addr}"
            ram[key]=f"{val}"
        return

    def output(val):
        nonlocal out_fifo
        out_fifo.append(f"{val}")
        return


    done = False
    while not done:
        cmd = get_command(ic)
        op = get_opcode(cmd);
        a, b, c, a_mode, b_mode, c_mode = get_params_and_modes(cmd);
        if op == "01":                              #ADD
            a = get_addr(a,a_mode)
            b = get_addr(b,b_mode)
            set_addr(c,a+b,c_mode)
            ic += 4
        elif op == "02":                            #MULTIPLY
            a = get_addr(a,a_mode)
            b = get_addr(b,b_mode)
            set_addr(c,a*b,c_mode)
            ic += 4
        elif op == "03":                            #INPUT
            if in_fifo:
                set_addr(a,get_input(),a_mode)
                ic += 2
            else:
                #input fifo is empty so exit with resumable state
                done=True
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
            set_addr(c, 1 if a<b else 0 ,c_mode)
            ic += 4
        elif op == "08":                            #EQ
            a = get_addr(a,a_mode)
            b = get_addr(b,b_mode)
            set_addr(c, 1 if a==b else 0 ,c_mode)
            ic += 4
        elif op == "09":                            #ADJUST Relative Base (RB)
            a = get_addr(a,a_mode)
            rb += a
            ic += 2
        elif op == "99":                            #EXIT
            done = True
        else:
            print(f"ERROR: UNKNOWN OP CODE ({op}) @ {ic} -- CMD = {cmd}");
            done = True

        ### SANITY CHECKING
        if ic < 0:
            print("ERROR: IC Underflow - Simulating Normal Termination")
            op = "99" 
            done = True

        if ic >= len(prog):
            print("ERROR: IC Overflow - Simulating Normal Termination")
            op = "99" 
            done = True

    print(ram)
    return ",".join(prog), ic, op



def permute(items=[],partial=[],final=[]):
    if items:
        for i  in range(0,len(items)):
            item = items[i]
            final = permute( list(set([item]) ^ set(items)),partial + [item],final)
    else:
        final.append(partial)
    return final

with open("data/boost") as f:
    for listing in f:
        in_fifo = [2]
        out_fifo = []
        print(run_prog(listing,0,in_fifo,out_fifo))
        print(out_fifo)
