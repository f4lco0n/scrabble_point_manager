import random
class Option():
	def __init__(self):
		self.file = [line.rstrip('\n').upper() for line in open('dictionary.txt', "r")]	



	SCRABBLES_SCORES = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                    (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z"), (11, "Ą Ć Ę Ł Ń Ó Ś Ź Ż")]
	global LETTER_SCORES 
	LETTER_SCORES = {letter: score for score, letters in SCRABBLES_SCORES
                 for letter in letters.split()}

	def score_from_word(self,word):
		score = 0
		for w in word.upper():
			if w in LETTER_SCORES.keys():
				score += LETTER_SCORES.get(w)
		return score

	def score_from_file(self):
		return max(sum(LETTER_SCORES[c] for c in word) for word in self.file)


	def word_from_score(self,score):
		valid_words = [word for word in self.file if sum([LETTER_SCORES[letter] for letter in word ]) == score]
		if len(valid_words) != 0:
			print(random.choices(valid_words))
		else:
			print('')

				

