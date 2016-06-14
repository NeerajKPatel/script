import time

maxRec = 1000
fiboSeries = {}
for i in range(1, maxRec, 1):
	fiboSeries[i] = -1


def fiboMem(numb):
	if numb > maxRec:
		return "Max Recurse, unable to use memorizatio"
	elif numb < 2 :
		return numb
	elif fiboSeries[numb] != -1:
		return fiboSeries[numb]
	else:
		fiboSeries[numb] = fiboMem(numb-1) + fiboMem(numb-2)
		return fiboSeries[numb]

if __name__ == '__main__':
	t1 = time.time()
	## Range will be from 1 till maxRec and will increment by 1 
	for i in range(1, maxRec, 1):
		print "fibo(",i,")",fiboMem(i)
		#print "Number is: ",str(i), "Fibo Series would be", fiboMem(i), " in ",
	print "%.3f" % (time.time()-t1)," secs"
