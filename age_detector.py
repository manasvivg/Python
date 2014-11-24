age = input('Cuantos Anos tienes:')
if age < 5:
    ans= 'baby!!!'
elif age <= 10:
    ans = 'kid'
elif age <= 12:
    ans = 'tween'
elif age <= 19:
    ans = 'tweenager'
else:
    ans = 'fat lazy bum!!!!!!!!'

print 'you are a ' + ans
