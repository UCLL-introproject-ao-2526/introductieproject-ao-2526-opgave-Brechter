from hashlib import sha1

desired_value = "10ceee87f8b145ab495c3bca73b94455970159c6"
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letterlist = [0, 0, 0, 0, 0, 0, 0]
found = False
while not found:
    password = ''
    for i in letterlist:
        password += letters[i]
    print(password)
    hashed = sha1(password.encode())
    if hashed.hexdigest() == desired_value:
        pass_found = password
        found = True
    else:
        j = 0
        while letterlist[j] == 25:
            letterlist[j] = 0
            j += 1
        letterlist[j] += 1
print(pass_found)