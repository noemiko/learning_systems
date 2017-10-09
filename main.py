from sys import stdin

data= []
for line in stdin:
    line = line.split(',')
    line.pop(0)
    data.append(list(map(int, line)))
print (data)
