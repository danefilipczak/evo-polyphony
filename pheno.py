'''
module for phenotype functionality
A score is encoded very 
A genotype is a two dimensional array that holds the parts at the upper level and the pitch values.

Pitch values are encoded as integers from 0 - 19, 
which represents an octave and and fifth within whatever the range of the part is.
21 represents a rest, and 20 represents a continuation of the note before it.
woohoo
'''

import random  
import copy
mutationRate = 0.05
import music21 as m21
from fitness import *
from overlay import overlayScores

class Phenotype:
	def __init__(self, genes, template_):
		self.phenotype = None
		self.fitness = None
		self.score = None
		self.genotype = genes
		self.template = template_
		
	def evaluate(self):
		self.fitness = getParsimony(self.phenotype) + getConsonance(self.phenotype)


	def develop(self):

		# make the genetic score
		translation = self.translate()

		translation = self.scale(translation)

		# overlay the template on top
		self.phenotype = overlayScores(translation, self.template)
		timeSig = self.template.flat.getElementsByClass(m21.meter.TimeSignature)[0]
		# self.phenotype.parts[0].measures[0].insert(0, timSig)
		self.phenotype.insert(0, timeSig)

	def scale(self, score):
		'''
				put your parts into acceptable ranges
		'''
		scalars = [60, 55, 48, 40]

		for i in range(0, len(score.parts)):
			score.parts[i].transpose(scalars[i], inPlace=True)

		return score


	def translate(self):
		'''
				translate thy genotype into a score.
				for now, each voice is treated identically. 
		'''
		score = m21.stream.Score()
		for chromosome in self.genotype:
			part = m21.stream.Part()
			for gene in chromosome:

				if gene<=19 or len(part)<1:
					#push in an eigth note
					note = m21.note.Note()
					note.pitch.ps = gene
					note.quarterLength = 0.5
					part.append(note)

				# elif gene is 20 or len(part)==0:
				# 	#rest
				# 	rest = m21.note.Rest()
				# 	rest.quarterLength = 0.5
				# 	part.append(rest)



				elif gene is 20:
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
					if random.random() < 0.318:
						voice[i] = 20
					else:
						voice[i] = random.randint(0, 19)
		

		return mutant



		


