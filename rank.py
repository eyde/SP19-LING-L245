import sys

# creates empty dictionary
vocab = {}

hs = open('wiki.hist', 'r')
# for each of the lines of input
for line in hs.readlines(): 
    # the form is the line without spacing
	form = line.strip()
	row=form.split(' ')
    # if we haven't seen it yet, set the frequency count to 0
	if len(row) > 1:
		vocab[row[1]] = int(row[0])


freq = []

for w in vocab:
	freq.append((vocab[w], w))

freq.sort(reverse=True)

rank = 1
min = freq[0][0]
ranks = []
for i in range(0, len(freq)): 
	if freq[i][0] < min: 
		rank = rank + 1
		min = freq[i][0]
	ranks.append((rank, freq[i][0], freq[i][1]))

hs.close()

for i in ranks:
	print(i)

