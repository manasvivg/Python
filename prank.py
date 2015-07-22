import os
import re

def rename_files():
    path = "/Users/mario/Documents/Python/prank/"
    files = os.listdir(path)
    for x in files:
        if x[0] != '.':
            orig= path+x
            sub= re.sub(r'[0-9]+',r'',path+x)
            #print orig, sub
            os.rename(orig,sub)
rename_files()
