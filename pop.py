
from pheno import Phenotype
import music21 as m21
import random

popSize = 10
elitism = 3 #how many of the best survive at each generation


class Population:

    def __init__(self, score):
        self.template = score
        self.phenotypes = []
        # the length of a genotype is the 'eighthLength' of the score
        length = self.template.quarterLength*2
        numVoices = len(self.template.parts)
        i = 0
        #initialize population with random genes
        for i in range(0, popSize)
        	genotype = []
        	for j in range(0, numVoices):
				genotype.append([])
				for k in range(0, int(length)):
					genotype[j].append(random.randint(0, 21))
            self.phenotypes.append(Phenotype(genotype, self.template))

    def getFittest(self):
    	#should return a score
        pass

    def develop(self):
        '''
                develop every phenotype that has not yet been developed (attach a score to it)

        '''
        for p in self.phenotypes:
        	if p.phenotype is None:
        		p.develop()

    def evaluate(self):
        '''

                evaulate the fitness of every phenotype that has not already had its fitness evaluated

        '''
        for p in self.phenotypes:
        	if p.fitness is None:
        		p.evaluate()

    def nextGen(self):
        '''

                wipe out the least fit specimens and replace them with mutated versions of the better ones

        '''
        # the array by fitness

        #sort the phenotypes by their fitness in descending order
       	self.phenotypes.sort(key=lambda x: x.fitness, reverse=True)
       	#delete the worst ones
       	del self.phenotypes[-(len(self.phenotypes)-elitism):]


       	i = 0
       	while len(self.phenotypes)<popSize:
       		#make a new genotype that's a mutation of one of the elites
       		spawn = self.phenotypes[i].mutate()
       		self.phenotypes.append(Phenotype(spawn, self.template))
       		i+=1
       		i%=elitism


if __name__ == '__main__':
    score = m21.corpus.parse('bach/bwv67.4')
    p = Population(score)
    print(p.phens[0].genotype)
