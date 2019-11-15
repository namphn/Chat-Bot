import nltk
from nltk.stem.lancaster import LancasterStemmer
stememer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import random
import json

with open("intents.json") as file:
    data = json.load(file)
print()
