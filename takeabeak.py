import webbrowser
import time

i=0
print("this program started at: "+time.ctime())
while i < 3 :
    time.sleep(60*60*2)
    webbrowser.open("http://www.youtube.com/watch?v=ToVIlrfpBAA")
    i+=1
