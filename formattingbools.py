import csv
with open('spaces_all_test.csv') as test, open('spaces_all_test_bool.csv', 'w+') as testB, open('spaces_all_train.csv') as train, open('spaces_all_train_bools.csv', 'w+') as trainB:
	test = csv.reader(test)
	train = csv.reader(train)
	trainB = csv.writer(trainB)
	testB = csv.writer(testB)
	for r in train:
		#print r[2]
		i = [2,3,4,5,6,7,8,9,10,11,12,13]	
		bools = []
		for ind in i:
			if r[ind] == 't':
				bools.append(True)	
			else:
				bools.append(False)
		rw = [r[0]] + [r[1]] + bools
		trainB.writerow(rw)	
	
