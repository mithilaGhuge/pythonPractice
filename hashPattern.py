#printing pattern

i=1
while i<5:
    print("# ",end="")
    j=1
    while j<4:
        print("# ",end="")
        j+=1
    i+=1
    print()

for i in range(5):
    for j in range(5):
        print("* ", end="")
    print()