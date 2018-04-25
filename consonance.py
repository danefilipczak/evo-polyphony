'''
module for evaluating the consonance of any given voicing

'''


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

	integers = list(range(1, 101))

	fundamental = (1*ratios[interval])

	
	harmonics = []
	for i in range(1, 101):
		harmonics.append(fundamental*i)

	#print(harmonics)
	#print(integers)

	print(len(set(harmonics).intersection(set(integers)))/100)




def main():
	#major sixth is wonky, and tritone
	#similarity(9)


	#the ninth is more consonant than the second because, while they both have the same number of harmonics that coincide with the fundamental, the second has more that clash.

	harmonics = []
	for i in range(1, 100):
		harmonics.append((9/8)*i)

	print(harmonics)



if __name__ == '__main__':
	main()