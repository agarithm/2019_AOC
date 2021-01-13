
passwords = 0;
for pwd in range(359282,820402,1):
    repeats = False;
    sequential = False;
    pwd = f"{pwd}"
    if "00" in pwd:
        repeats = True;
    elif "11" in pwd:
        repeats = True;
    elif "22" in pwd:
        repeats = True;
    elif "33" in pwd:
        repeats = True;
    elif "44" in pwd:
        repeats = True;
    elif "55" in pwd:
        repeats = True;
    elif "66" in pwd:
        repeats = True;
    elif "77" in pwd:
        repeats = True;
    elif "88" in pwd:
        repeats = True;
    elif "99" in pwd:
        repeats = True;

    tmp = [char for char in pwd]
    tmp.sort()
    tmp = "".join(tmp)
    sequential = tmp == pwd;
    if(sequential & repeats):
        passwords+=1

print(f"Valid Passwords = {passwords}")
       



passwords = 0;
for pwd in range(359282,820402,1):
    repeats = False;
    sequential = False;
    pwd = f"{pwd}"
    if "00" in pwd and not "000" in pwd:
        repeats = True;
    elif "11" in pwd and not "111" in pwd:
        repeats = True;
    elif "22" in pwd and not "222" in pwd:
        repeats = True;
    elif "33" in pwd and not "333" in pwd:
        repeats = True;
    elif "44" in pwd and not "444" in pwd:
        repeats = True;
    elif "55" in pwd and not "555" in pwd:
        repeats = True;
    elif "66" in pwd and not "666" in pwd:
        repeats = True;
    elif "77" in pwd and not "777" in pwd:
        repeats = True;
    elif "88" in pwd and not "888" in pwd:
        repeats = True;
    elif "99" in pwd and not "999" in pwd:
        repeats = True;

    tmp = [char for char in pwd]
    tmp.sort()
    tmp = "".join(tmp)
    sequential = tmp == pwd;
    if(sequential & repeats):
        passwords+=1

print(f"Valid Passwords = {passwords}")
       



