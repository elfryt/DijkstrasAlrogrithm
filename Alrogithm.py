a = 1
achild1 = 3
achild2 = 1
b = 3
bchild1 = 4
bchild2 = 2
c = 4					#change values here
path = 0
	
def compareAchild():
	if achild1 < achild2:
		path = "a, a.child1"	#compare achild1 and achild2
		print(path)		#shows shortest path
	elif achild2 < achild1:
		path = "a, a.child2"
		print(path)
		
def compareBchild():
	if bchild1 < bchild2:
		path = "b, bchild1"
		print(path)
	elif bchild2 < bchild1:
		path = "b, bchild2"
		print(path)

if a < b and achild1 + achild2 < bchild1 + bchild2:
	compareAchild()			#calls to compare
	
elif b < a and bchild1 + bchild2 < achild1 + achild2:
	compareBchild()
