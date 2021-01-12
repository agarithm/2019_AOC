
def filler(mass):
    fuel = 0;
    if int(mass) <= 0:
        return 0
    else:
        fuel = int(mass)//3-2
        if fuel < 0:
            return 0
        else:
            return fuel + filler(fuel)

fuel = int(0);
with open("data/fuel") as f:
    for mass in f:
        fuel = fuel + (int(mass)//3) - 2

print(f"Fuel Needed = {fuel}")


fuel = int(0);
with open("data/fuel") as f:
    for mass in f:
        fuel = fuel + filler(mass)

print(f"Fuel Needed = {fuel}")
