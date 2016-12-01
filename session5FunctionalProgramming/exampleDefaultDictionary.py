# We want to count the words in a sentence
sentence = "The quick brown fox is a fox that is quick and brown"

wordCount = {}

for word in sentence.split(" "):
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1

print wordCount


class wordCounter(dict):
    def __getitem__(self, key):
        if key in self:
            return dict.__getitem__(self, key)
        else:
            dict.__setitem__(self, key, 0)
            return self[key]
wordCount = wordCounter()

for word in sentence.split(" "):
    wordCount[word] += 1

print wordCount
