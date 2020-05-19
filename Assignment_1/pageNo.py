page_nums = list(range(1, 26))
def scanNum():
	a = []
	nums = raw_input("Enter input- ")
	for n in nums.split():
    		n = int(n)
		if n > 25 or n < 0:
			print("Invalid input")
			return 0
    		a.append(n)
	return a
temp = scanNum()
if(temp != 0) :
	pageNo = list(set(page_nums)-set(temp))
	print("Missing page Numbers : ")
	print(pageNo)


