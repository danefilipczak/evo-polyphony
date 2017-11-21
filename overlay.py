'''
module for overlaying the contents of a score onto another score.
Intended for polyphonic music, only works on note objects
'''


import music21 as m21
import copy


def overlayPart(z0_, z1):
	z0 = copy.deepcopy(z0_).flat.notes.stream()
	'''
			z0 is the "far" score that will be overlayed upon.
			z1 is the "near" score that will overlay z0
	'''
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

	return z0.makeMeasures()


if __name__ == '__main__':
	z0 = m21.converter.parse('tinynotation: 4/4 A B C G G F')
	z1 = m21.converter.parse('tinynotation: 4/4 r D8 E r G A')
	z0.show()
	z1.show()
	overlayPart(z0, z1).show()