FILE = "input.txt"

inp = open(FILE,"r").readline().strip()
inp = str(bin(int(inp, 16)))[2:].zfill(len(inp)*4)

total = 0

def decode(s):
    global total
    if len(s) < 6:
        return ""
    version = int(s[:3], 2)
    total += version
    pid = int(s[3:6], 2)
    s = s[6:]
    if pid == 4:
        out_string = ""
        while True:
            out_string += s[1:5]
            finished = not int(s[0])
            s = s[5:]
            if finished:
                break

    else:
        length_id = s[0]
        s = s[1:]
        if length_id == "0":
            bits_in_subpackets = int(s[0:15], 2)
            s = s[15:]
            subpackets = s[:bits_in_subpackets]
            s = s[bits_in_subpackets:]
            while subpackets:
                subpackets = decode(subpackets)
        
        elif length_id == "1":
            num_of_subpackets = int(s[0:11])
            s = s[11:]
            for i in range(num_of_subpackets):
                s = decode(s)
    return s

            

print(decode(inp))
print(total)