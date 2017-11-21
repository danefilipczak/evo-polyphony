'''
module for phenotype functionality
A score is encoded very 
A genotype is a two dimensional array that holds the parts at the upper level and the pitch values.

Pitch values are encoded as integers from 0 - 19, 
which represents an octave and and fifth within whatever the range of the part is.
20 represents a rest, and 21 represents a continuation of the note before it.
woohoo
'''

import random
import copy
mutationRate = 0.05

class Phenotype:
	def __init__(self, genes, template_):
		self.phenotype = None
		self.fitness = None
		self.score = None
		self.genotype = genes
		self.template = template_
		
	def evaluate(self):



	def develop(self):
		# copy the template
		self.phenotype = copy.deepcopy(self.template)


	def mutate(self):
		'''
			return a mutated version of your own genotype
		'''
		mutant = copy.deepcopy(self.genotype)

		for voice in mutant:
			for i in range(0, len(voice)):
				if random.random() < mutationRate:
					voice[i] = random.randint(0, 21)
		


		return mutant



		


