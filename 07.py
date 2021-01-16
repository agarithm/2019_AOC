
def run_prog(listing,ic=0,in_fifo=[],out_fifo=[]):
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
        nonlocal in_fifo;
        return int(in_fifo.pop(0))

    def get_addr(addr,mode=0):
        nonlocal prog
        return addr if mode else int(prog[addr])


    def set_addr(addr,val):
        nonlocal prog
        prog[addr]=f"{val}"
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
            set_addr(c,a+b)
            ic += 4
        elif op == "02":                            #MULTIPLY
            a = get_addr(a,a_mode)
            b = get_addr(b,b_mode)
            set_addr(c,a*b)
            ic += 4
        elif op == "03":                            #INPUT
            if in_fifo:
                set_addr(a,get_input())
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
            set_addr(c, 1 if a<b else 0 )
            ic += 4
        elif op == "08":                            #EQ
            a = get_addr(a,a_mode)
            b = get_addr(b,b_mode)
            set_addr(c, 1 if a==b else 0 )
            ic += 4
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

    return ",".join(prog), ic, op


def run_chain(listing,chain):
    value = 0;
    while chain:
        setting = chain[0]
        chain = chain[1:]
        in_fifo = [setting,value]
        out_fifo = []
        run_prog(listing,0,in_fifo,out_fifo)
        value = int(out_fifo.pop())
    return value


def permute(items=[],partial=[],final=[]):
    if items:
        for i  in range(0,len(items)):
            item = items[i]
            final = permute( list(set([item]) ^ set(items)),partial + [item],final)
    else:
        final.append(partial)
    return final

permutations = permute([0,1,2,3,4])

max_thrust = 0;
max_perm = []
with open("data/amplifiers") as f:
    for listing in f:
        for perm in permutations:
            thrust = run_chain(listing,perm)
            print(f"THRUST = {thrust} - {perm}")
            max_perm = perm if thrust > max_thrust else max_perm
            max_thrust = thrust if thrust > max_thrust else max_thrust


print(f"MAX THRUST = {max_thrust} - {max_perm}")



###############################
###############################


def run_feedback(listing,perm):
    a_out = []
    b_out = []
    c_out = []
    d_out = []
    e_out = []
    a_in = e_out
    b_in = a_out
    c_in = b_out
    d_in = c_out
    e_in = d_out
    a_in.append(perm[0])
    b_in.append(perm[1])
    c_in.append(perm[2])
    d_in.append(perm[3])
    e_in.append(perm[4])
    a_in.append(0)
    a_ic = 0;
    b_ic = 0;
    c_ic = 0;
    d_ic = 0;
    e_ic = 0;
    a_listing = listing
    b_listing = listing
    c_listing = listing
    d_listing = listing
    e_listing = listing
    a_op = ""
    b_op = ""
    c_op = ""
    d_op = ""
    e_op = ""
    while not e_op == "99":
        a_listing, a_ic, a_op = run_prog(a_listing,a_ic,a_in,a_out)
        b_listing, b_ic, b_op = run_prog(b_listing,b_ic,b_in,b_out)
        c_listing, c_ic, c_op = run_prog(c_listing,c_ic,c_in,c_out)
        d_listing, d_ic, d_op = run_prog(d_listing,d_ic,d_in,d_out)
        e_listing, e_ic, e_op = run_prog(e_listing,e_ic,e_in,e_out)
    return int(e_out.pop())

permutations = permute([5,6,7,8,9])

max_thrust = 0;
max_perm = []
with open("data/amplifiers") as f:
    for listing in f:
        for perm in permutations:
            thrust = run_feedback(listing,perm)
            print(f"THRUST = {thrust} - {perm}")
            max_perm = perm if thrust > max_thrust else max_perm
            max_thrust = thrust if thrust > max_thrust else max_thrust


print(f"MAX THRUST = {max_thrust} - {max_perm}")



