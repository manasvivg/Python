#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

#match=re.search(r'.*[_][a-z|0-9]+[_].*',"place_code.google.com")

def get_special_paths(dir):

  #find special files
  special = []
  for dir1 in dir:
    filenames = os.listdir(dir1)
    for file in filenames:
      match=re.search(r'.*[_][a-z|0-9]+[_].*',file)
      if match:
        special += [os.path.join(dir1, file)]

  return special


def copy_to(paths,dir):
  if not os.path.exists(dir):
    os.mkdir(dir)
  for files in paths:
    shutil.copy(files, dir)
  return


def zip_to(paths, zippath):
  for files in paths:
    cmd = 'zip -j ' + zippath +' ' + files
    print "trying:", cmd
    (status, output) = commands.getstatusoutput(cmd)
    print "status=",status, "output=", output
    if status:    ## Error case, print the command's output to stderr and exit
      sys.stderr.write(output)
      sys.exit(1)
  return


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  paths=get_special_paths(args)
  if todir:
    copy_to(paths,todir)
  if tozip:
    zip_to(paths,tozip)

if __name__ == "__main__":
  main()
