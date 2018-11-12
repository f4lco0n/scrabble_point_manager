import unittest
from option import Option

class TestOption(unittest.TestCase):

	def setUp(self):
		self.option = Option()

	def test_score_from_word(self):
		result = self.option.score_from_word("KOT")
		self.assertEqual(result,7)

	def test_score_from_word_lower(self):
		result = self.option.score_from_word("kot")
		self.assertEqual(result,7)


	def test_score_from_word_different_letter(self):
		result = self.option.score_from_word("KOt")
		self.assertEqual(result,7)

	def test_score_from_file(self):
		result = self.option.score_from_file()
		self.assertEqual(result,97)

				
if __name__ == '__main__':
	unittest.main()
