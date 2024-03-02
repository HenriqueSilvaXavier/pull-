def pull(x, y):
	zlista=[]
	Zlista=[]
	for k in x:
		zlista.append(k)
	for k in y:
		Zlista.append(k)
	indices=[]
	for k in range(0, len(zlista)):
		if zlista[k] in Zlista:
			a=Zlista.index(zlista[k])
			Zlista.pop(a)
			indices.append(k)
	c=0
	for k in indices:
		zlista.pop(k-c)
		c=c+1
	if type(x)==str and type(y)==str:
		n=""
		for k in zlista:
			n=n+k
		return n
	elif type(x)==list and type(y)==list:
		return zlista