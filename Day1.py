# Day1AoC2017
# Written by: Alexis Renderos	
f = open('Day1Input.txt', 'r')

for line in f:
    file = line.split()

file[0] = file[0] + file[0][0]

i = 0
k_sum = 0

print(file[0])

while i < (((len(file[0]))-1)):
	e1 = int(file[0][i])
	e2 = int(file[0][i+1])
	if e1 == e2:
		k_sum +=  (e1 + e2) / 2
	i = i + 1

print(k_sum)

#I haven't written python in quite a while.
