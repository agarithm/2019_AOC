def distance(move):
    return int(move[1:])

def trace(wire):
    x = 0;
    y = 0;
    trace = []
    for move in wire:
        dy = 0;
        dx = 0;
        dist = distance(move)
        print(f"{move} = {dist}");
        if move[0]=='D':
            for i in range(1, dist+1):
                dy = -i;
                trace.append(f"{x+dx},{y+dy}")
        if move[0]=='U':
            for i in range(1, dist+1):
                dy = i;
                trace.append(f"{x+dx},{y+dy}")
        if move[0]=='L':
            for i in range(1, dist+1):
                dx = -i;
                trace.append(f"{x+dx},{y+dy}")
        if move[0]=='R':
            for i in range(1, dist+1):
                dx = i;
                trace.append(f"{x+dx},{y+dy}")
        x = x + dx
        y = y + dy
    return trace

def manhattan(point):
    x,y = point.split(',');
    return (abs(int(x))+abs(int(y)));

with open("data/wires") as f:
    lines = f.readlines()
    wires = []
    traces = []
    for line in lines:
        wire = line.strip().split(",")
        wires.append(wire)
    for wire in wires:
        traces.append(trace(wire));

    overlap = list(set(traces[0]) & set(traces[1]))
    min_dist = 100000000000000000000000
    min_point = ''
    print(overlap)
    for point in overlap:
        m = manhattan(point)
        if m > 0 and m < min_dist:
            min_dist =  m
            min_point = point
            print(f"{point} {m} {min_dist}")

    print(f"MANHATTAN = {min_dist} @ {min_point}")
    
    min_steps = 100000000000000000000000
    for point in overlap:
        a = traces[0].index(point)+1;
        b = traces[1].index(point)+1;
        steps = a+b
        print(f"{steps} = {a} {b}")
        if steps < min_steps and steps > 0 :
            min_steps = a+b


    print(f"MIN STEPS = {min_steps}")
