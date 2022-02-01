l1 = [int(line.strip()) for line in open("1.in")]
print(sum( 1 for i in range(1, len(l1)) if l1[i] > l1[i-1] ))

