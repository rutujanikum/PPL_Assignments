def amc(a) :
	i = 1
	sum1 = 0
	sum2 = 0
	while(i < a) :
		if(a % i == 0):
			sum1 = sum1 + i
		i = i + 1
	i = 1
	while(i < sum1) :
                if(sum1 % i == 0):
                        sum2 = sum2 + i
		i = i + 1
	if(a == sum2 and a != sum1):
		return 1, sum1
	else :
		return 0, 0
cnt = 0
a = 1
while(cnt <= 10) :
	l1 = amc(a)
	if(l1[0] == 1):			
		print(a, l1[1])
		a = l1[1] + 1
		cnt = cnt + 1
	a = a + 1

