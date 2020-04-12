# 10.2 Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time
# and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 2 :
    name = "mbox-short.txt"
handle = open(name)
c = dict()
for line in handle :
    if line.startswith('From ') :
        t = line.split()[5].split(":")
        c[t[0]] = c.get(t[0], 0) + 1 # add time to dictionary
#print(sorted(c.items()))
for k, v in sorted(c.items()) :
    print(k, v)
