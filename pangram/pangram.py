import string

def is_pangram(sentence):
	return all(s in sentence.lower() for s in string.ascii_lowercase)