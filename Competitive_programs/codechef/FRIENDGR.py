def solve(n,k,s):
	ans = [i for i in range(n) if s[i] == "1"]

	if ans == []:
		print(0)
		return

	c = 1
	ans[0] += 1
	for i in range(1,len(ans)):
		if abs((ans[i]+1)-ans[i-1]) <= k:
			ans[i] += 1
		elif abs(ans[i]-ans[i-1]) <= k:
			pass
		elif abs((ans[i]-1)-ans[i-1]) <= k:
			ans[i] -= 1
		else:
			ans[i] += 1
			c += 1
	print(c)

for _ in range(int(input())):
	n,k = map(int,input().split())
	s = input()
	solve(n,k,s)
