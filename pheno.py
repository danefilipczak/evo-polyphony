'''
module for phenotype functionality
A score is encoded very 
A genotype is a two dimensional array that holds the parts at the upper level and the pitch values.

Pitch values are encoded as integers from 0 - 19, 
which represents an octave and and fifth within whatever the range of the part is.
20 represents a rest, and 21 represents a continuation of the note before it.
woohoo
'''

class Phenotype:
	def __init__(self):
		self.fitness = None
		self.score = None
		
	

