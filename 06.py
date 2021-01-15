orbits = {}
addrs = {}
with open("data/orbits") as f:
    for line in f:
        a, b = line.strip().split(")")
        addrs[b] = a
        if a in orbits:
            orbits[a].append(b)
        else:
            orbits[a] = [b]

def count_orbits(orbits, planet = 'COM', depth = 1):
    count = len(orbits[planet])*depth if planet in orbits else depth
    for next in orbits[planet]:
        if next in orbits:
            count += count_orbits(orbits, next, depth+1)

    return count

print(f"All Orbits = {count_orbits(orbits)}")

def get_path(planet,addrs):
    out = []
    if planet in addrs:
            out = [addrs[planet]]
            out += (get_path(addrs[planet],addrs))
    
    return out

route = set(get_path('YOU',addrs)) ^ set(get_path('SAN',addrs))

print(f"ROUTE = {route}")
print(f"LENGTH = {len(route)}")
