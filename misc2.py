xfile = open('test.txt')
for i in xfile:
    print(i, end = '')
inp = xfile.read()
print(len(inp))
