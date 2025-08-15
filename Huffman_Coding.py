with open("Para.txt","r") as f:
    a = f.read()
    ch = {}
    for i in a:
        if i not in ch.keys():
            ch[i] = 1
        else:
            ch[i] += 1

    print(ch.items())