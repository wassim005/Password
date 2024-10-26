from random import choice

def createpass(data):
    password = ""
    char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890?!,.$%_-&"
    for i in range(data):
        password += choice(char)
    return f"Your password is : {password}"


print("=============================")
print(createpass(8))
print("=============================")