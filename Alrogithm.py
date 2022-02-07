a = 1
achild1 = 3
achild2 = 1
b = 3
c = 4					#change values here
path = 0
	
def compareAchild():
	if achild1 < achild2:
		path = "a, a.child1"	#compare achild1 and achild2
		print(path)		#shows shortest path
	elif achild2 < achild1:
		path = "a, a.child2"
		print(path)

if a < b:
	compareAchild()			#calls to compare
