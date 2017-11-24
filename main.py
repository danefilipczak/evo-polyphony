# we'll stop the program running if the fitness gets this high.
terminationFitness = 0

from pop import Population
from pheno import Phenotype
import music21 as m21

def main(score):
    # make a new population suitable to evolve this particular score
    population = Population(score)
    fitness = -100000000000  # some rediculous arbitrarily low fitness
    count = 0
    generation = 0
    while fitness < terminationFitness:
        population.develop()
        population.evaluate()
        population.nextGen()
        fitness = population.fittest.fitness
        generation+=1
        print('generation #', generation)
        print('highest fitness', fitness)

        population.fittest.phenotype.write("musicxml", "output/generation" + str(generation) + ".xml")



def debug(score):
	# score.show()
	p = Population(score)
	p.develop()
	p.evaluate()
	p.nextGen()

	# phen = Phenotype(p.randomGenotype(), p.template)
	# print(phen.genotype)
	# phen.develop()
	# phen.phenotype.show()

if __name__ == '__main__':
    score = m21.converter.parse("input/test2.xml")
    # main(score)
    main(score)
