comp = ['c=', 'c-', 'dz=','d-', 'lj', 'nj', 's=', 'z=']

str = input()

for a in comp:
	str = str.replace(a, "_")
    
print(len(str))