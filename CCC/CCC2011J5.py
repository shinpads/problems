n = int(input())
friend = [[] for i in range(n+1)]
for i in range(1,n):
	x = int(input())
	friend[x].append(i)

def getval(x):
	
	if len(friend[x]) == 0:
		return 2	
	m = 1
	for f in friend[x]:
		m*=getval(f)
	return 1+m

print(getval(n)-1)
