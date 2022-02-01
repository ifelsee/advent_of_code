l1 = [0,0]
for line in open("2.in"):
	line = line.strip()
	line = line.split()
	line[1] = int(line[1])	
	if line[0] == "forward": l1[0] += line[1] 
	elif line[0] == "down": l1[1] -= line[1]
	elif line[0] == "up": l1[1] += line[1]
	

print(abs(l1[0]*l1[1]))
