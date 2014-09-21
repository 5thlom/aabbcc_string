def fun(s):
	c =0
	ss = s[0]
	d = ''
	for data in s:
		if ss==data:
			c+=1
		else:
			d=d+ss+str(c)
			ss=data
			c=1
	d = d+ss+str(c)
	return d

def fun2(s):
	if s=='':
		return '',0

	rv = fun2(s[1:])
	if rv==s[0]:



print fun('hhhelloooooo')