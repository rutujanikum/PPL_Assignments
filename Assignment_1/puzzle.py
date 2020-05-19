def insert1(obj) :
	l.append(obj)
		
def remove1(obj) :
	l.append(obj)

ml = ["tiger","grass","goat"]
vl1 = ["+goat","+grass","-goat","+tiger","+goat"]
vl2 = ["+goat","+tiger","-goat","+grass","+goat"]
cnt = 0
ch = 1
l = []
print("Objects : Tiger, Grass, Goat")
print("Enter 1 to cross river")
print("Enter 2 to take back")
print("Enter 0 to exit")
while(cnt < 5 and ch != 0) :
	ch = int(input("Choice : "))
	if(ch == 1) :
		obj = raw_input("Enter object to insert : ")
		obj = "+"+obj
		insert1(obj)
		cnt = cnt+1
		#print(cnt)
		#print(l)		
	if(ch == 2) :
		obj = raw_input("Enter object to remove : ")
		obj = "-"+obj
		remove1(obj)
		cnt = cnt+1
		#print(cnt)
		#print(l)
if(l == vl1 or l == vl2) :
	print("Congratulations")
else :
	print("loser")
