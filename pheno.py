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
import music21 as m21

from overlay import overlayScores

class Phenotype:
	def __init__(self, genes, template_):
		self.phenotype = None
		self.fitness = None
		self.score = None
		self.genotype = genes
		self.template = template_
		
	def evaluate(self):



	def develop(self):

		# make the genetic score
		translation = self.translate()

		translation = self.scale(translation)

		# overlay the template on top

		self.phenotype = overlayScores(translation, self.template)

	def scale(self, score):
		'''
				put your parts into acceptable ranges
		'''
		scalars = [60, 55, 48, 40]

		for i in range(0, len(score.parts)):
			score.parts[i].transpose(scalars[i], inPlace=True)

		return score


	def translate():
		'''
				translate thy genotype into a score.
				for now, each voice is treated identically. 
		'''
		score = m21.stream.Score()
		for chromosome in self.genotype:
			part = m21.stream.Part()
			for gene in chromosome:

				if gene<=19:
					#push in an eigth note
					note = m21.note.Note()
					note.pitch.ps = gene
					part.append(note)

				elif gene is 20:
					#rest
					part.append(rest)
				elif gene is 21:
					#continue the last element
					part[-1].quarterLength+=0.5
			score.insert(0, part)

		return score


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



		


