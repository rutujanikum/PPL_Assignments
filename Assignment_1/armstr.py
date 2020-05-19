def armstr(a) :
	n = a
	sum1 = 0
	num = 0
	while n > 0:
		num = n % 10
		n = n / 10
		sum1 = sum1 + num**3
	return sum1

print("Enter Range : ")
f = int(input("From : "))
t = int(input("To : "))
a = list(range(f, t+1))
flag = 0
for n in a:
	sum1 = armstr(n)
	if(sum1 == n):
		flag = 1
                print(n," is Armstrong Number")
if(flag == 0):
	print("No armstrong number from ",f," to ",t)
		
