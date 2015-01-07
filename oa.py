import csv
with open('underground_probabilites.csv') as undg:
	undg = csv.reader(undg)
	c1 = 0
	c2 = 0
	c3 = 0
	next(undg)
	for row in undg:
		c1 += 1
		if(float(row[1]) > 0.1 and float(row[1]) < 0.9):	
			c2 += 1
		if(float(row[1]) > 0.25 and float(row[1]) < 0.75):
			c3 += 1
	#va = c2 / c1
	#print "the % of spaces in the interval are " + str(va)
	print c3
	print c2 
	print c1
	
