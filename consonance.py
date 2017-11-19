import music21 as m21


consonanceScalar = 2
# score = m21.converter.parse('evotest.xml')

score = m21.corpus.parse('bach/bwv66.6')

fitness = 0

chords = score.chordify()

#get the time signature
for e in score.flat:
	if isinstance(e, m21.meter.TimeSignature):
		timeSig = e.ratioString
		break

print(timeSig)


for c in chords.recurse().getElementsByClass('Chord'):
    if not c.isConsonant():
    	fitness -= c.beatStrength * consonanceScalar
        # print(c.measureNumber, c.beatStrength, c.beatStr, c)

print(fitness)

#chords.show()