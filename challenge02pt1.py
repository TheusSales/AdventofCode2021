horizontal=0
depth=0

input = open('input.txt','r')

line = input.readline()

while line:
    edit = (line.strip("\n")).split(" ")
    command = edit[0]
    amount = int(edit[1])

    if command == "forward":
        horizontal+=amount
    elif command == "up":
        depth-=amount
    elif command == "down":
        depth+=amount
    line=input.readline()
input.close()

print(horizontal,depth)
print(depth*horizontal)