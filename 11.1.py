import re

name = input("Enter file:")
if len(name) < 1 :
    name = "regex_sum_403256.txt"
handle = open(name)
l = list()
for line in handle:
    line = line.strip()
    dig = re.findall('[0-9]+', line) # find all digits

    for x in dig :
        if x != None: # convert all 'str' in founded list to 'int', append to list l and sum
            x = int(x)
            l.append(x)

    result = sum(l)
print(result)
