
class Population:

    def __init__(self, score):
        self.input = score
        self.individuals = []

    def say_hi(self):
        print('Hello, my name is', self.name)

    def getFittest(self):
        pass
        # return

    def develop(self):
        '''
                develop every phenotype that has not yet been developed (attach a score to it)

        '''
        pass

    def evaluate(self):
        '''

                evaulate the fitness of every phenotype that has not already had its fitness evaluated

        '''
        pass

    def nextGen(self):
        '''

                wipe out the least fit specimens and replace them with mutated versions of the better ones

        '''
        # the array by fitness
        pass


# def getFittest:
    '''
	returns the score of the fittest phenotype
	'''
