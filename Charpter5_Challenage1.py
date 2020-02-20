import random

"""
Create a program to show a random list of words,
if some words are duplicate, only show one
"""

# Create a list of words
wordList = ["facility","grief","access","killer","snake",
            "invasion","laborer","beautiful","repeat","ambition",
            "plot","blue","responsible","dramatic","quota",
            "mushroom","excitement","law","hurt","qualify",
            "facility","grief","access","killer","snake",
            "invasion","laborer","beautiful","repeat","ambition",
            "plot","blue","responsible","dramatic","quota",
            "mushroom","excitement","law","hurt","qualify",
            ]

# For random part
# Option 1, use random.sample
print("Size of world list: " + str(len(wordList)))
sample_worldList = random.sample(wordList,len(wordList))
print("Size of random world list" + str(len(sample_worldList)))
print(random.sample(wordList,len(wordList)))

# Option 2, use random.shuffe
random.shuffle(wordList)
print("Shuffe the list:")
print(wordList)

# For unique part
# Option 1, use set
worldList_set = set(wordList)
set_worldList = list(worldList_set)
print(set_worldList)

# Option use numpy.unique
import numpy as np
unique_worldList = np.unique(wordList)
print(unique_worldList)