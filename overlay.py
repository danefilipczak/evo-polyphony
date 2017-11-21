'''
module for overlaying the contents of a score onto another score.
Intended for polyphonic music, only works on note objects.
Assumes many things, namely that each score has the same number of parts. 
'''


import music21 as m21
import copy


def overlayParts(z0_, z1):
	'''
			z0 is the "far" score that will be overlayed upon.
			z1 is the "near" score that will overlay the other
	'''
	z0 = copy.deepcopy(z0_).flat.notesAndRests.stream()
	for note in z1.flat.notes:
		# get the offset of note
		start = note.offset
		end = start + note.quarterLength
		# split the thing in z1 at that offset
		z0 = z0.sliceAtOffsets([start, end], addTies=False)
		# z0.show('text')
		toDelete = z0.getElementsByOffset(start, end, includeEndBoundary=False)
		for d in toDelete:
			z0.remove(d)
		# insert note into z0
		z0.insert(start, note)

	return z0

def overlayScores(z0, z1):
	'''
			Given two scores, return the notes of z1 overlayed on top of the notes of z0
	'''
	result = m21.stream.Score()
	for i in range(0,  len(z1.parts)):
		part = overlayParts(z0.parts[i], z1.parts[i])
		# part.show()
		result.insert(0, part)



	return result



if __name__ == '__main__':
	z0 = m21.corpus.parse('bach/bwv67.4')
	z1 = m21.converter.parse('input/z1.xml')
	s = overlayScores(z0, z1)
	# s.insert(1, m21.tempo.MetronomeMark("slow", 40, m21.note.Note(type='half')))
	z0.show()
	s.show()