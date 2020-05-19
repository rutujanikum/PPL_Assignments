def harmonic(a) :
	cnt = 0.0
	i = 1.0
	sum1 = 0.0
	res = 0.0
	while(i <= a) :
		if(a % i == 0) :
			sum1 = sum1 + (1/i)
			cnt = cnt + 1
		i = i + 1
	res = cnt/sum1
	return res.is_integer()

cnt = 0
a = 1.0
b = 0
while(cnt <= 10) :
	if(harmonic(a)) :
		b = a
		print(b)
		cnt = cnt + 1
	a = a + 1
