# https://www.reddit.com/r/dailyprogrammer/comments/4so25w/20160713_challenge_275_intermediate_splurthian/

def assignsymbols():
	dict = {}

	def findsymbol(el):
		"""Finds best symbol, saves it to d and return True, or False otherwise"""
		i, j = 0, 1
		while i < len(el)-1:
			while j < len(el):
				proposal = el[i] + el[j]
				if not proposal in dict:
					dict[proposal] = 1
					return True
				j += 1
			i += 1
			j = i + 1
		return False

	with open('sporith.txt', 'r') as f:
	    for element in f:
				if not findsymbol(element.rstrip().lower()):
				    print element
				    break

assignsymbols()