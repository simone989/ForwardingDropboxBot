d ={
		"key":"response",
		"lol":[
		{
			"new":"Lol"
		},
		{
			"new" :"xD"
		}
	]
} 

print (d.keys())
listfile = d.get(("lol"))
print (listfile[0])

for pr in listfile:
	if(isinstance(pr, dict)):
		for m in pr.items():
			print (m)
print ("\n")
for x in d.items():
	print (x)
	if (isinstance(x,(list,dict))):
		for f in x:
			print (f)
