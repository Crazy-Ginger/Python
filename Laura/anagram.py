from collections import Counter
from sys import argv
print([word[1] for word in [(Counter(word), word) for word in open("wordList.txt", "rt").read().split("\n") if len(word) == sum(Counter(argv[1]).values())] if word[0] == Counter(argv[1])])
