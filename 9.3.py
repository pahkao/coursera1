# 9.4 Write a program to read through the mbox-short.txt and
# figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number
# of times they appear in the file. After the dictionary is produced,
# the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)
list = list()
counts = dict()
for line in handle :
    if not line.startswith('From:') :
        continue
    words = line.split()
    #print(words)
    for x in words :
        if x != 'From:' :
            counts[x] = counts.get(x, 0) + 1

#print(counts)

bigcount = -1
bigword = None
for k,v in counts.items() :
    #print(k,v)
    if v > bigcount  :
        bigcount = v
        bigword = k

print(bigword,bigcount)


#if bigcount is None or count > bigcount:
    #    bigcount = word
    #    bigword = count


#print(counts)
#counts[x] = counts.get(x, 0) + 1
