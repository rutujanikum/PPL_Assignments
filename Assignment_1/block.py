site = raw_input()
flag = 0
file = open("ritu.txt", "r")
line = file.read()
if(line.__contains__(site)):
		flag = 1
if(flag == 0) :
	print("Accessible ")
else :
	print("Not Accessible")
