#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/



"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""
import sys
import re


def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  f=open(filename)
  data = f.read()
  f.close()
  match=re.search(r'(Popularity in\s)+(\d+)',data)
  year=match.group(2)

  tuples=match=re.findall(r'(?:<td>)(\d+)(?:</td><td>)([A-Z][a-z]+)(?:</td><td>)([A-Z][a-z]+)',data)
  dictm={x[0]:x[1] for x in tuples}
  dictf={x[0]:x[2] for x in tuples}
  dict = dictm.items()+dictf.items()
  tuples = [(y[1],y[0]) for y in dict]
  tuples.sort()
  list1 = [year]
  for x in tuples:
    list1.append(x[0]+" "+x[1])

  return list1


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  #your code here
  for filename in args:
    names = extract_names(filename)
    text = '\n'.join(names)
    if not summary:
      print text
    if summary:
      match=re.search(r"([a-z]+[0-9]+)(?:[\.html])",filename)
      out1 = match.group(1) + "_summary.txt"
      out_f = open(out1,'w')
      out_f.write(text+'\n')
      out_f.close()

if __name__ == '__main__':
  main()
