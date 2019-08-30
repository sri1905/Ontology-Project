done = [5,7,8,27,53,59,66,67,
	26,29,30,68,72,81,82,86,
	44, 58, 63, 73, 77, 85,

	10,22,25,31,32,33,34,36,37,40,42,43,45,46,48,49,50,51,52,55,56,57,65,75,89,91,92,94,97,98,99,100,

	]
cnt = 0
done.sort()
print done
for i in range(1,101):
	if not (i in done):
		print i
		cnt = cnt+1

print "\nremaining - ",
print cnt

    
