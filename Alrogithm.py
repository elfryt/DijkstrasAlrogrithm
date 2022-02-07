a = 1
a.child1 = 3
a.child2 = 4
b = 3
c = 4									#change values here
S = 0
E = 0

if a < b:
	compareA.child()
	
compareA.child():
	if a.child1 < a.child2:
		E = 'a, a.child1'
		console.log(E)
	elseif a.child2 < a.child1:
		E = 'a, a.child2'
		console.log(E)
