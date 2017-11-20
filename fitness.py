'''
k
defines fitness function for scores.
fitness is a combination of consonance, conjunct melodic motion, and limited macroharmony

'''


import music21 as m21
import math 


consonanceScalar = 2
parsimonyScalar = 0.005
# score = m21.converter.parse('evotest.xml')



# fitness = 0



#get the time signature
# for e in score.flat:
# 	if isinstance(e, m21.meter.TimeSignature):
# 		timeSig = e.ratioString
# 		break



def getConsonance(s):
	'''
	given a score, return a score representing how consonant the downbeats are.
	Depends on the beatStrength attribute of global time signatures.
	'''
	fitness = 0
	chords = s.chordify()
	for c in chords.recurse().getElementsByClass('Chord'):
	    if not c.isConsonant():
	    	fitness -= c.beatStrength * consonanceScalar
	    	# print(c.measureNumber, c.beatStrength, c.beatStr, c.commonName)
	return fitness


def getParsimony(s):
	fitness = 0
	for part in s.getElementsByClass('Part'):
		notes = part.flat.notes
		for i in range(0, len(notes)-1):
			interval = m21.interval.notesToChromatic(notes[i], notes[i+1])
			fitness-=2**(abs(interval.semitones))
	return fitness * parsimonyScalar

def labelParsimony(s):
	fitness = 0
	for part in s.getElementsByClass('Part'):
		notes = part.flat.notes
		for i in range(0, len(notes)-1):
			interval = m21.interval.notesToChromatic(notes[i], notes[i+1])
			notes[i].addLyric(interval.semitones)
	s.show()
	return fitness * parsimonyScalar


	


if __name__ == '__main__':
	score = m21.corpus.parse('bach/bwv67.4')
	fitness = getConsonance(score) + getParsimony(score)
	print([fitness, getConsonance(score), getParsimony(score)])
	labelParsimony(score)




# score.show()
#chords.show()