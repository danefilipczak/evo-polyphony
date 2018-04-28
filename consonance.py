'''
module for evaluating the consonance of any given voicing

'''
import math
import itertools

def similarity(interval):
	'''
			return the harmonic similarity of an interval, expressed in semitones
	'''
	ratios = [
	1/1,
	16/15,
	9/8,
	6/5,
	5/4,
	4/3,
	1.4,
	3/2,
	8/5,
	5/3,
	9/5,
	15/8
	]

	integers = list(range(1, 1001))

	fundamental = ratios[interval%12]*math.pow(2, math.floor(interval/12))

	
	harmonics = []
	for i in range(1, 101):
		harmonics.append(fundamental*i)

	#print(harmonics)
	#print(integers)
	match = 0
	mismatch = 0
	for h in harmonics:
		if h in integers:
			match+=1
		else:
			mismatch+=1
	# print('match', match)
	# print('mismatch', mismatch)

	return (match-mismatch)/len(harmonics)

	#print(len(set(harmonics).intersection(set(integers)))/100)


def percentageSimilarity(x, y):
	'''
		((x+y-1)/(x*y))*100, where x is the numerator of the frequency ratio and y is the denominator of the ratio.
	'''
	return ((x+y-1)/(x*y))*100


def consonance(array):
	total = 0
	for i in itertools.combinations(array, 2):
		total+=similarity(abs(i[1]-i[0]))
		print(i, similarity(abs(i[1]-i[0])))
	return total/len(array)

def main():
	#major sixth is wonky, and tritone
	#similarity(9)


	'''the ninth is more consonant than the second because, 
	while they both have the same number of harmonics that coincide with the fundamental, 
	the second has more that clash.
	'''

	# harmonics = []
	# for i in range(1, 100):
	# 	harmonics.append((6/2)*i)

	# print(harmonics)

	# print(similarity(2))
	# print(similarity(14))
	# print(similarity(14+24))
	print(consonance([0, 7, 16]))
	#print(percentageSimilarity(12, 5))



if __name__ == '__main__':
	main()