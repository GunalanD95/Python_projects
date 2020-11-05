fname = "python_nw.py"

with open (fname,"w") as x:
	x.write("GUNA D")
	x.close()

with open (fname,"r") as x:
	print(x.read())

