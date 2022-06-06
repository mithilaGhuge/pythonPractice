x = [10, '1', 20, '4']
for i in x:
    if type(i) != int:
        x.remove(i)
        x.append(int(i))
print(x)

print(sorted(x))