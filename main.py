# we'll stop the program running if the fitness gets this high.
terminationFitness = -10

from pop import Population
from pheno import Phenotype
import music21 as m21

def main(score):
    # make a new population suitable to evolve this particular score
    population = Population(score)
    fitness = -100000000000  # some rediculous arbitrarily low fitness
    count = 0
    # while fitness < terminationFitness:
    #     population.develop()
    #     population.evaluate()
    #     population.nextGen()
    #     fitness = population.getHighestFitness()

    #     # save the fittest to disk every 100 generations
    #     count += 1
    #     count %= 100
    #     if count is 0:
    #         population.getFittest().write("musicxml", "output/fittest.xml")



def debug(score):
	# score.show()
	p = Population(score)
	p.develop()
	p.evaluate()
	for phen in p.phenotypes:
		print(phen.fitness)
	# phen = Phenotype(p.randomGenotype(), p.template)
	# print(phen.genotype)
	# phen.develop()
	# phen.phenotype.show()

if __name__ == '__main__':
    score = m21.converter.parse("input/test1.xml")
    # main(score)
    debug(score)
