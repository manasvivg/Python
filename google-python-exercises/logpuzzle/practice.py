#Practice exercises
import os
import re
import sys
import urllib


f = open("/Users/mario/Documents/Python/google-python-exercises/logpuzzle/animal_code.google.com","rU")
data=f.read()
#([.]+[puzzle]+[.])(?:[HTTP])
puzzles=re.findall(r'(?:GET)(.+puzzle.+)(?: HTTP)',data)
print length(puzzles)
