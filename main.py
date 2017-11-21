# we'll stop the program running if the fitness gets this high.
terminationFitness = -10


def main(score):
    # make a new population suitable to evolve this particular score
    population = Population(score)
    fitness = -100000000000  # some rediculous arbitrarily low fitness
    count = 0
    while fitness < terminationFitness:
        population.develop()
        population.evaluate()
        population.nextGen()
        fitness = population.getHighestFitness()

        # save the fittest to disk every 100 generations
        count += 1
        count %= 100
        if count is 0:
        	population.getFittest().write("musicxml", "output/fittest.xml")








if __name__ == '__main__':
    main(score)
