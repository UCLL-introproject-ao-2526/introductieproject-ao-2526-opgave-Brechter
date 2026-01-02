file = open(r"Challenges\information-theory\03-representing-data\07-base64\mystery.jpeg.base64", "r")
text_enc = file.read()
def make_num(text_enc):
    text_bin = ''
    for i in text_enc:
        num = ord(i)
        if 64 < num < 91:
            nnum = num - 65
        elif 96 < num < 123:
            nnum = num - 97 + 26
        elif 47 < num < 58:
            nnum = num + 4
        elif num == 43:
            nnum = 62
        elif num == 47:
            nnum = 63
        else:
            nnum = 100
        text_bin = make_bin(nnum, text_bin)
    return text_bin

def make_bin(num, text_bin):
    nl = ''
    if not num == 100:
        i = 5
        while i >= 0:
            if num > 2**i:
                nl += '1'
                num -= 2**i
            else:
                nl += '0'
            i -= 1
    else:
        nl = '='
    text_bin += nl
    return text_bin

def remove_red(text_bin):
    j = -1
    red = 0
    while text_bin[j] == "=":
        red -= 3
        j -= 1
    text_bin = text_bin[:red]
    return text_bin

def decode_bin(text_bin):
    text_dec = ''
    for i in range(7, len(text_bin), 7):
        inst = text_bin[(i-7):i]
        num = 0
        for j in inst:
            num = num*2
            num += int(j)
        ltr = chr(num)
        text_dec += ltr
    return text_dec

text_bin = make_num(text_enc)
text_bin = remove_red(text_bin)
text_dec = decode_bin(text_bin)
print(text_dec)