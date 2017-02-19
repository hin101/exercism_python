from collections import defaultdict
import re

def word_count(word):
    result = defaultdict(int)
    words = re.sub("[\W]|_"," ", word, re.UNICODE)

    for word in words.lower().split():
        result[word] += 1

    return result
