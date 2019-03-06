import sys

# creates empty list
vocab = []

hs = open('wiki.hist', 'r')
# for each of the lines of input
for line in hs.readlines(): 
    # the form is the line without spacing
	form = line.strip()
	row=form.split(' ')
    # if we haven't seen it yet, set the frequency count to 0
	if len(row) > 1:
		vocab.append(row[1])

for line in sys.stdin.readlines():
	lines=line.split(' ')
	for x in lines:
		if x in vocab:
			print(x)
		else:
			print("*"+x)

hs.close()

