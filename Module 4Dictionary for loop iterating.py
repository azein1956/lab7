letterFreq = {'a': 195, 'r': 22, 'e':256, 't': 166, 'l': 103, 'x': 2}
rareLetters = []
for lettKey in letterFreq:
    freq = letterFreq[lettKey]
    print("Letter", lettKey, "occurred", freq, "times")
    if freq < 30:
        rareLetters.append(lettKey)
print("Infrequent letters:", rareLetters)