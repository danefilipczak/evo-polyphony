'''
class for analyzing voice leading properties of scores (that must have parts in them)

Adapted from parts of the 'theory analyizer' tool from the  music21-tools repository
https://github.com/cuthbertLab/music21-tools/blob/master/theoryAnalysis/theoryAnalyzer.py

'''


import music21 as m21


class VoiceLeadingAnalyzer:

	def __init__(self):
		self.store = {}
		self.result = []

	def getVLQs(self, score, partNum1, partNum2):

		from music21 import tree
		tsCol = tree.fromStream.asTimespans(score,
		                                    flatten=True,
		                                    classList=(m21.note.Note, m21.chord.Chord))
		allVLQs = []
		defaultKey = None

		for v in tsCol.iterateVerticalities():
		    vlqs = v.getAllVoiceLeadingQuartets(
		        partPairNumbers=[(partNum1, partNum2)])
		    for vlq in vlqs:
		        newKey = vlq.v1n1.getContextByClass('KeySignature')
		        # if newKey is None:
		        #     if defaultKey is None:
		        #         defaultKey = score.analyze('key')
		        #     newKey = defaultKey
		        # vlq.key = newKey

		    allVLQs.extend(vlqs)
		return allVLQs

	def _identifyBasedOnVLQ(self, score, partNum1, partNum2, dictKey,
		                        testFunction, textFunction=None,
		                        color=None, editorialDictKey=None,
		                        editorialValue=None, editorialMarkList=None):

		result = []
		if editorialMarkList is None:
			editorialMarkList = []


	    # self.addAnalysisData(score)
		if partNum1 is None or partNum2 is None:
			for (pN1, pN2) in self.getAllPartNumPairs(score):
				self._identifyBasedOnVLQ(score, pN1, pN2, dictKey, testFunction,
					textFunction, color, editorialDictKey,
					editorialValue, editorialMarkList)
		else:

		    vlqList = self.getVLQs(score, partNum1, partNum2)
		    # if endIndex is None and startIndex >= 0:
		    #     endIndex = len(vlqList)

		    for vlq in vlqList:
			    
			    if testFunction(vlq) is not False:  # True or value
			    	# print(vlq)
				    # tr = theoryResult.VLQTheoryResult(vlq)
				    # tr.value = testFunction(vlq)
				    # if textFunction is None:
				    #     tr.text = tr.value
				    # else:
				    #     tr.text = textFunction(vlq, partNum1, partNum2)
				    # if editorialDictKey != None:
				    #     tr.markNoteEditorial(
				    #         editorialDictKey, editorialValue, editorialMarkList)
				    # if color is not None:
				    #     tr.color(color)
				    # self._updateScoreResultDict(score, dictKey, tr)
			    	self.result.append(vlq)

		# print(result)
		# return result


	def getAllPartNumPairs(self, score):
	    '''
	    Gets a list of all possible pairs of partNumbers:
	    tuples (partNum1, partNum2) where 0 <= partNum1 < partnum2 < numParts

	    '''
	    partNumPairs = []
	    numParts = len(score.parts)
	    for partNum1 in range(numParts - 1):
	        for partNum2 in range(partNum1 + 1, numParts):
	            partNumPairs.append((partNum1, partNum2))

	    return partNumPairs

	def getParallelFifths(self, score, partNum1=None, partNum2=None):
	    self.result = []
	    '''
	    Identifies all parallel fifths in score, or only the parallel fifths found between
	    partNum1 and partNum2, and
	    returns these as instances of :class:`~music21.voiceLeading.VoiceLeadingQuartet`
	    '''
	    sid = score.id
	    testFunction = lambda vlq: vlq.parallelFifth()
	    return self._identifyBasedOnVLQ(score, partNum1, partNum2, dictKey='parallelFifths',
	                        testFunction=testFunction)

	    # if self.store[sid]['ResultDict'] and 'parallelFifths' in self.store[sid]['ResultDict']:
	    #     return [tr.vlq for tr in self.store[sid]['ResultDict']['parallelFifths']]
	    # else:
	    #     return None

if __name__ == '__main__':
	score = m21.converter.parse('input/parallelTest1.xml')
	vla = VoiceLeadingAnalyzer()
	vla.getParallelFifths(score)
	print(len(vla.result))
