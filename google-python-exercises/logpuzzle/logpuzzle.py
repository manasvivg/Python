#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

#sorted1 = sorted(puzzles,key=key1)



def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  path = os.getcwd()
  f = open(os.path.join(path,filename),"rU")
  data= f.read()
  f.close()
  server = re.match(r'(?:.+_)(.+)',filename).group(1)
  puzzles=re.findall(r'(?:GET )(.+puzzle.+)(?: HTTP)',data)
  key1=[]
  for p in puzzles:
    key1.append(re.search(r'(.+)-(.+)-(.+)\.(.+)',p).group(3))

  together = zip(key1,puzzles)
  together_sort = sorted(together)
  sorted1 = [x[1] for x in together_sort]
  unique = []
  [unique.append(item) for item in sorted1 if item not in unique]

  index=0
  for u in unique:
    unique[index] = 'http://' + server + unique[index]
    index+=1

  return unique

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  i = 0
  path = os.getcwd() + "/" + dest_dir
  if not os.path.exists(path):
    os.mkdir(path)

  sys.stdout.write('image: ')
  sys.stdout.flush()
  #download files
  for url in img_urls:
    sys.stdout.write(str(i)+'..')
    sys.stdout.flush()
    if "image" in urllib.urlopen(url).info().gettype():
      file_type = re.search(r'(.+\.)(.+)',url).group(2)
      urllib.urlretrieve(url,os.path.join(path,  "img"+str(i)+"."+file_type))
      i += 1

  print '\r'

  #create index file
  out = open(os.path.join(path,'index.html'),'w')
  out.write('<verbatim>'+ '\n')
  out.write('<html>'+ '\n')
  out.write('<body>'+ '\n')
  part1 = '<img src="/Users/mario/Documents/Python/google-python-exercises/logpuzzle/'+dest_dir+'/img'

  for x in range(i-1):
    out.write(part1+str(x)+"."+file_type+'">')
  out.write('\n')
  out.write('</body>'+ '\n')
  out.write('</html>'+ '\n')
  out.close()
  return

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
