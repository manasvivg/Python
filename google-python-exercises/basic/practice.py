#Practice exercises

hash = {}
hash['word'] = 'garfield'
hash['count'] = 42
hash['word'] = 'charlie brown'
hash['count'] = 50
print hash
s = 'I want %(count)d copies of %(word)s' % hash
print s
