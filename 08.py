

width = int(input("Image Width: "))
height = int(input("Image Height: "))
area = width * height
raw_layers = []
with open("data/password") as f:
    for password in f:
        password = password.strip()
        min_count_0 = area
        answer = 0
        while len(password) > 0:
            raw_layers.append(password[:area])
            password = password[area:]
        for layer in raw_layers:
            print( layer)
            if layer.count("0") < min_count_0:
                min_count_0 = layer.count("0")
                answer = layer.count("1") * layer.count("2")

        print(f"ANSWER: {answer}")


final = {}
for layer in raw_layers:
    for i in range(0,area):
        if not layer[i] == "2":
            key = f"{i}"
            if not key in final:
                final[key] = layer[i]

for i in range(0,height):
    line = ""
    for j in range(0,width):
        key = f"{i*width+j}"
        line = f"{line}{'*' if final.get(key)=='1' else ' '}"
    print(f"{line}")
