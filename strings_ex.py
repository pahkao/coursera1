# Write code using find() and string slicing (see section 6.10)
# to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.
text = "X-DSPAM-Confidence:    0.8475"
pos1 = text.find(':')
#print(pos1)
res1 = text[pos1+1:]
#print(res1)
res = res1.lstrip()
print(res)
