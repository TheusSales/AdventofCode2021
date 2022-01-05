horizontal=0
depth=0
aim=0

input = open('input.txt','r')

line = input.readline()

while line:
    edit = (line.strip("\n")).split(" ")
    command = edit[0]
    amount = int(edit[1])

    if command == "forward":
        depth=aim*amount+depth
        horizontal+=amount
    elif command == "up":
        aim-=amount
    elif command == "down":
        aim+=amount
    line=input.readline()
input.close()

print("horizontal = ", horizontal)
print("depth = ", depth)
print("aim = ",aim)
print("depth*horizontal = ",depth*horizontal)
